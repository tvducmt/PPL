
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
    
    def getName(self, decl):
        return decl.variable.name if isinstance(decl, VarDecl) else  decl.name.name
    
    def getType(self, decl):
        if isinstance(decl, VarDecl):
            return decl.varType
        else:
            return MType([i.varType for i in decl.param] , decl.returnType)
                
    def visitProgram(self,ast, c):
        scopeProg = self.global_envi
        for i in ast.decl:
            temp = Symbol(self.getName(i),self.getType(i))
            if isinstance(i, VarDecl):
                if self.lookup(i.variable.name, scopeProg, lambda x: x.name):
                    raise Redeclared(i.varType, i.variable.name)
                else:
                    scopeProg.insert(0,temp)
            else:
                if self.lookup(i.name.name, StaticChecker.global_envi, lambda x: x.name):
                    if isinstance(i.returnType, VoidType):
                        raise Redeclared(Procedure(), i.name.name)
                    else:
                        raise Redeclared(Function(), i.name.name)
                else:
                    temp = Symbol(self.getName(i),self.getType(i))
                    scopeProg.insert(0, temp)
                
        return [self.visit(x,scopeProg) for x in ast.decl]

    def visitVarDecl(self, ast, param):
        return Symbol(ast.variable.name, ast.varType)

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
                raise Redeclared(Variable(), u.variable.name)
            else:
                scopeFuncDecl.insert(0, Symbol(u.variable.name, u.varType))
        scopeFuncDecl=scopeFuncDecl+ c
        #print([self.visit(x,scopeFuncDecl) for x in ast.body])
        return [self.visit(x,(scopeFuncDecl, True)) for x in ast.body]
    
 
    def visitCallExpr(self, ast, c):
        at = [self.visit(x,(c[0],False)) for x in ast.param]
        print(at)
        res = self.lookup(ast.method.name,c[0],lambda x: x.name)
        if res is None or not type(res.mtype) is MType or not type(res.mtype.rettype) is VoidType:
            raise Undeclared(Procedure(),ast.method.name)
        elif len(res.mtype.partype) != len(at):
            raise TypeMismatchInExpression(ast)            
        else:
            return res.mtype.rettype
    
#     def checkType(self, lhs, rhs):
#         if (type(lhs),type(rhs)) == (FloatType,IntType):
#             return True
#         else:
#             if isinstance(type(lhs), type(rhs)):
#                 return True
#             else:
#                 return False

#     def visitIntLiteral(self,ast, c): 
#         return IntType()

#     def visitFloatLiteral(self, ast, c):
#         return FloatType()
    
#     def visitBooleanLiteral(self, ast, c):
#         return BoolType()
    
#     def visitStringLiteral(self, ast, c):
#         return StringType()

#     def visitId(self, ast, c):
#         if  not self.lookup(ast.name, c, lambda x: x.name):
#             raise Undeclared(Identifier(), ast.name)
       