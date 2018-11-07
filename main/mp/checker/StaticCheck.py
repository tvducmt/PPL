
"""
 * @author nhphung
"""
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype
    def __str__(self):
        return 'Mtype(['+','.join(str(i) for i in self.partype) + '],'+str(self.rettype) + ')';

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value
    def __str__(self):
        return 'Symbol('+str(self.name)+','+str(self.mtype)+')';

class StaticChecker(BaseVisitor,Utils):

    global_envi =   [Symbol("getInt",MType([],IntType())),
                    Symbol("putInt",MType([IntType()],VoidType())),
                    Symbol("putIntLn",MType([IntType()],VoidType())),
                    Symbol("getFloat",MType([],FloatType())),
                    Symbol("putFloat",MType([FloatType()],VoidType())),
                    Symbol("putFloatLn",MType([FloatType()],VoidType())),
                    Symbol("putBool",MType([BoolType()],VoidType())),
                    Symbol("putBoolLn",MType([BoolType()],VoidType())),
                    Symbol("putString",MType([StringType()],VoidType())),
                    Symbol("putStringLn",MType([StringType()],VoidType())),
                    Symbol("putLn",MType([],VoidType()))] 

    
    def __init__(self,ast):
        self.ast = ast
   
    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)
    
    # def checkRedeclared(self, name, kind, evn):
    #     if self.lookup(name, evn, lambda x: x.name):
    #         raise Redeclared(kind, sym.name)
    def getName(self, decl):
        return decl.variable.name if isinstance(decl, VarDecl) else  decl.name.name
    
    def getType(self, decl):
        if isinstance(decl, VarDecl):
            return decl.varType
        else:
            return MType([i.varType for i in decl.param] , decl.returnType)
                
    def visitProgram(self,ast, c):
        scopeProg = self.global_envi
        main     = None 
        for i in ast.decl:
            temp = Symbol(self.getName(i),self.getType(i))
            if isinstance(i, VarDecl):
                if self.lookup(i.variable.name, scopeProg, lambda x: x.name):
                    raise Redeclared(i.varType, i.variable.name)
                else:
                    scopeProg.insert(0,temp)
            else:
                if self.lookup(i.name.name, StaticChecker.global_envi, lambda x: x.name):
                    if type(i.returnType) == VoidType:
                        raise Redeclared(Procedure(), i.name.name)
                    else:
                        raise Redeclared(Function(), i.name.name)
                else:
                    
                    if type(i.returnType) == VoidType and i.name.name == 'main':
                        main = i
                    temp = Symbol(self.getName(i),self.getType(i))
                    scopeProg.insert(0, temp)
        if main is None:
            raise NoEntryPoint()
        return [self.visit(x,scopeProg) for x in ast.decl]

    def visitVarDecl(self, ast, param):
        pass
        #return Symbol(ast.variable.name, ast.varType)

    def visitFuncDecl(self,ast, c): 
       
        #Tham số của hàm
        scopeProg = c
        scopeFuncDecl = []
        for i in ast.param:
            if self.lookup(i.variable.name, scopeFuncDecl, lambda x: x.name):
                raise Redeclared(Parameter(), i.variable.name)
            else:
                scopeFuncDecl.insert(0, Symbol(i.variable.name, i.varType))
    
        for u in ast.local:
            if self.lookup(u.variable.name, scopeFuncDecl, lambda x: x.name):
                raise Redeclared(self.getType(u), u.variable.name)
            else:
                scopeFuncDecl.insert(0, Symbol(u.variable.name, u.varType))
        scopeFuncDecl=scopeFuncDecl+ c

        [self.visit(x,(scopeFuncDecl,False)) for x in ast.body]
        


        
    def checkType(self, lhs, rhs):
        if (type(lhs),type(rhs)) == (FloatType,IntType):
            return True
        else:
            if type(lhs) == type(rhs):
                return True
            else:
                return False
        
    def visitAssign(self, ast, c):
        env = c[0]
        exp = self.visit(ast.exp, env)    
        lhSymbol = self.lookup(ast.lhs.name, env, lambda x: x.name)
        if not lhSymbol :
            raise Undeclared(Identifier(), ast.lhs.name)
        else:
            if lhSymbol.mtype == (StringType or ArrayType):
                raise TypeMismatchInStatement(ast)
            else:
                if not self.checkType(lhSymbol.mtype, exp):
                    raise TypeMismatchInStatement(ast)
                else:
                    return 

    def visitIf(self, ast, c): # oked
        env = c[0]
        ifExp = self.visit(ast.expr, env)
        if type(ifExp) != BoolType :
            raise TypeMismatchInStatement(ast)
        [self.visit(x, env) for x in ast.thenStmt]
        if ast.elseStmt is not None:
            [self.visit(y, env) for y in ast.elseStmt]

    def visitFor(self, ast, c): # oked
        env = c[0]
        idType = self.visit(ast.id, env)
        expr1 = self.visit(ast.expr1, env)
        expr2 = self.visit(ast.expr2, env)
        if idType != expr1 or idType != expr2 or type(expr1) != IntType or type(expr2) != IntType:
            raise TypeMismatchInStatement(ast)
        else:
            isEnd = False
         # visit each stmt (env,reT,B/C)
            for st in ast.loop:
                if isEnd is True or isEnd is "BC":
                    raise UnreachableStatement(st)
                isEnd = self.visit(st,(env,True))
                print(isEnd)
            #isRet.append(isEnd)
            #[self.visit(x, (env, True)) for x in ast.loop]

    def visitWhile(self, ast, c):
        env = c[0]
        Expr = self.visit(ast.Expr, env)
        if Expr != BoolType :
            raise TypeMismatchInStatement(ast)
        else:
            [self.visit(x, (env, True)) for x in ast.sl]

    def visitReturn(self, ast, c):
        env = c[0]
        for x in env:
            if isinstance(x.mtype,MType):
                break;
        
        if ast.expr is None and x.mtype.rettype == VoidType():
            return True
        elif ast.expr is None and x.mtype.rettype == VoidType():
            raise TypeMismatchInStatement(ast)
        else:
            returnType = x.mtype.rettype
            returnExp = self.visit(ast.expr, env)
            if (returnType ,returnExp) == (FloatType,IntType):
                return True
            else:
                if returnType == returnExp:
                    return True
                else:
                    raise TypeMismatchInStatement(ast)
    def visitBreak(self, ast, c):
        if c[1] == False:
            raise BreakNotInLoop()
        return "BC"

    def visitContinue(self, ast, c):
        if c[1] == False:
            raise ContinueNotInLoop()
        return "BC"

    def visitBinaryOp(self, ast, c):
        env = c[0]
        left = self.visit(ast.left, env)
        right = self.visit(ast.right, env)
        if ast.op == '*' or ast.op == '+' or ast.op == '-' or ast.op == '/':
            if (left, right) == (IntType(), IntType()):
                return IntType()
            elif (left, right) == (IntType(), FloatType()):
                return FloatType()
            elif (left, right) == (FloatType(), FloatType()):
                return FloatType()
            elif (left, right) == ( FloatType() , IntType()):
                return FloatType()
            else:
                raise TypeMismatchInExpression(ast)
        elif ast.op == '<' or ast.op == '<=' or ast.op == '>' or ast.op == '>=' or ast.op == '<>' :
            if (left, right) == (IntType(), IntType()):
                return BoolType()
            elif (left, right) == (IntType(), FloatType()):
                return BoolType()
            elif (left, right) == (FloatType(), FloatType()):
                return BoolType()
            elif (left, right) == ( FloatType() , IntType()):
                return BoolType()
            else:
                raise TypeMismatchInExpression(ast)
        elif ast.op == '=':
            if (left, right) == (FloatType(), IntType()):
                return BoolType()
            elif (left, right) == (FloatType(), FloatType()):
                return BoolType()
            elif (left, right) == (BoolType(), BoolType()):
                return BoolType()
            elif (left, right) == (IntType(), IntType()):
                return BoolType()
            elif (left, right) == (StringType(), StringType()):
                return BoolType()
            else:
                raise TypeMismatchInExpression(ast)
        elif ast.op == 'div' or ast.op == 'mod':
            if (left, right) == (IntType(), IntType()):
                return IntType()
            else:
                raise TypeMismatchInExpression(ast)
        elif ast.op == 'and' or ast.op == 'or':
            if (left, right) == (BoolType(), BoolType()):
                return BoolType()
            else:
                raise TypeMismatchInExpression(ast)
        elif ast.op == 'andthen' or  ast.op == 'orelse':
            if (left, right) == (BoolType(), BoolType()):
                return BoolType()
            else:
                raise TypeMismatchInExpression(ast)
        else:
            print("sdgf1")

    def UnaryOp(self, ast, c):
        if ast.op == 'not':
            if self.visit(ast.body) == BoolType():
                return BoolType()
            else:
                raise TypeMismatchInExpression(ast)
        elif ast.op == '-':
            if self.visit(ast.body) == IntType():
                return IntType()
            elif self.visit(ast.body) == FloatType():
                return FloatType()
            else:
                raise TypeMismatchInExpression(ast)

    def visitCallStmt(self, ast, c): 
        at = [self.visit(x,(c[0],False)) for x in ast.param]
        
        res = self.lookup(ast.method.name,c[0],lambda x: x.name)
        if res is None or not type(res.mtype) is MType or not type(res.mtype.rettype) is VoidType:
            raise Undeclared(Procedure(),ast.method.name)
        elif len(res.mtype.partype) != len(at):
            raise TypeMismatchInStatement(ast)            
        else:
            return res.mtype.rettype

    def visitArrayCell(self, ast, c):
        arrType = self.visit(ast.arr, c)
        idx = self.visit(ast.idx, c)
        if type(arrType) != ArrayType or type(idx) != IntType:
           TypeMismatchInExpression(ast)
        else:
            return arrType.eleType

    def visitIntLiteral(self,ast, c): 
        return IntType()

    def visitFloatLiteral(self, ast, c):
        return FloatType()
    
    def visitBooleanLiteral(self, ast, c):
        return BoolType()
    
    def visitStringLiteral(self, ast, c):
        return StringType()

    def visitIntType(self, ast, c):
        return IntType()

    def visitFloatType(self, ast, c):
        return FloatType()

    def visitBoolType(self, ast, c):
        return FloatType()

    def visitStringType(self, ast, c):
        return StringType()
    
    def visitVoidType(self, ast, c):
        return VoidType()
    
    def visitId(self, ast, c):
        symbol = self.lookup(ast.name, c, lambda x: x.name) 
        if  not symbol:
            raise Undeclared(Identifier(), ast.name)
        else:
            if  (isinstance(symbol.mtype, MType)):
                raise Undeclared(Identifier(), ast.name)
            else:
                return symbol.mtype

