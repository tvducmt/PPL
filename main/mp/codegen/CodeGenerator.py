'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *   @name  Trần Văn Đức
 *   @Mssv    1510819
 *
'''
from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod
import functools 

class CodeGenerator(Utils):
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [    Symbol("getInt",MType([],IntType()), CName(self.libName)),
                    Symbol("putInt",MType([IntType()],VoidType()), CName(self.libName)),
                    Symbol("putIntLn",MType([IntType()],VoidType()), CName(self.libName)),
                    Symbol("getFloat",MType([],FloatType()), CName(self.libName)),
                    Symbol("putFloat",MType([FloatType()],VoidType()), CName(self.libName)),
                    Symbol("putFloatLn",MType([FloatType()],VoidType()), CName(self.libName)),
                    Symbol("putBool",MType([BoolType()],VoidType()), CName(self.libName)),
                    Symbol("putBoolLn",MType([BoolType()],VoidType()), CName(self.libName)),
                    Symbol("putString",MType([StringType()],VoidType()), CName(self.libName)),
                    Symbol("putStringLn",MType([StringType()],VoidType()), CName(self.libName)),
                    Symbol("putLn",MType([],VoidType()), CName(self.libName)),
                ] 

        # return [Symbol("getInt", MType(list(), IntType()), CName(self.libName)),
        #             Symbol("putInt", MType([IntType()], VoidType()), CName(self.libName)),
        #             Symbol("putIntLn", MType([IntType()], VoidType()), CName(self.libName))
                    
        #             ]

    def gen(self, ast, dir_):
        #ast: AST
        #dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)

# class StringType(Type):
    
#     def __str__(self):
#         return "StringType"

#     def accept(self, v, param):
#         return None

class ArrayPointerType(Type):
    def __init__(self, ctype):
        #cname: String
        self.eleType = ctype

    def __str__(self):
        return "ArrayPointerType({0})".format(str(self.eleType))

    def accept(self, v, param):
        return None
class ClassType(Type):
    def __init__(self,cname):
        self.cname = cname
    def __str__(self):
        return "Class({0})".format(str(self.cname))
    def accept(self, v, param):
        return None
        
class SubBody():
    def __init__(self, frame, sym):
        #frame: Frame
        #sym: List[Symbol]

        self.frame = frame
        self.sym = sym

class Access():
    def __init__(self, frame, sym, isLeft, isFirst):
        #frame: Frame
        #sym: List[Symbol]
        #isLeft: Boolean
        #isFirst: Boolean

        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst

class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        #value: Int

        self.value = value

class CName(Val):
    def __init__(self, value):
        #value: String

        self.value = value

class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "MPClass"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")
        self.curFunc = Symbol("null", MType([],VoidType()), CName(self.className))

    def visitProgram(self, ast, c):
        #ast: Program
        #c: Any

        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        
        
        lsFunc = list(filter(lambda x: type(x) is FuncDecl, ast.decl))
       
        for x in ast.decl:
            if type(x) is VarDecl:
                self.emit.printout(self.emit.emitATTRIBUTE(x.variable.name, x.varType, False, ""))
                symbol = Symbol(x.variable.name, x.varType, CName(self.className))
                self.env.append(symbol)
            else:
                typeFunc = MType([y.varType for y in x.param], x.returnType)
                symbol = Symbol(x.name.name, typeFunc, CName(self.className))
                self.env.append(symbol)
        
        e = SubBody(None, self.env)
        for x in lsFunc:
            self.visit(x, e)

        
        # generate default constructor
        self.genMETHOD(FuncDecl(Id("<init>"), list(), list(), list(),None), c, Frame("<init>", VoidType))
        self.emit.emitEPILOG()
        return c

    def genMETHOD(self, consdecl, o, frame):
        #consdecl: FuncDecl
        #o: Any
        #frame: Frame

        isInit = consdecl.returnType is None
        isMain = consdecl.name.name == "main" and len(consdecl.param) == 0 and type(consdecl.returnType) is VoidType
        returnType = VoidType() if isInit else consdecl.returnType
        methodName = "<init>" if isInit else consdecl.name.name
        intype = [ArrayPointerType(StringType())] if isMain else list()
        mtype = MType(intype, returnType)
        self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isInit, frame))

        frame.enterScope(True)

        
        lsVarLocal =[]
        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayPointerType(StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        else:
            for x in consdecl.param:
                self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), x.variable.name, x.varType, frame.getStartLabel(), frame.getEndLabel(), frame))
                lsVarLocal.append(Symbol(x.variable.name, x.varType,Index(frame.currIndex-1)))
        for y in consdecl.local:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), y.variable.name, y.varType, frame.getStartLabel(), frame.getEndLabel(), frame))
            lsVarLocal.append(Symbol(y.variable.name, y.varType,Index(frame.currIndex-1)))
        
       # glenv = o + lsVarLocal
        #print(o)
        glenv = lsVarLocal + (o if o != None else [])
            
        #f=========
        body = consdecl.body
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        if isInit:
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        
        list(map(lambda x: self.visit(x, SubBody(frame, glenv)), body))
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(returnType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        else:
            self.emit.printout(self.emit.emitRETURN(returnType, frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope();

    def visitVarDecl(self, ast, c):
        ctxt = c
        frame = ctxt.frame
        glenv = ctxt.sym 
        name = ast.variable.name
        mtype = ast.varType
        
        if frame is not None:
            idx = frame.getNewIndex()
            self.emit.printout(self.emit.emitVAR(idx, name, mtype, frame.getStartLabel(), frame.getEndLabel(), frame))
        return SubBody(frame, glenv.append(Symbol(name, mtype,Index(idx))))
        

    def visitFuncDecl(self, ast, o):
        #ast: FuncDecl
        #o: Any
        subctxt = o
        frame = Frame(ast.name, ast.returnType)
        self.curFunc = self.lookup(ast.name.name, subctxt.sym, lambda x: x.name)
        self.genMETHOD(ast, subctxt.sym, frame)
        return SubBody(None, [Symbol(ast.name, MType(list(), ast.returnType), CName(self.className))] + subctxt.sym)
    
    def visitAssign(self, ast, c):
        ctxt = c
        frame = ctxt.frame
        env = ctxt.sym
        str_I2f = ''
        (resExpr, typeExpr) = self.visit(ast.exp, Access(c.frame, c.sym, False, True ))
        (reslhs, typelhs) = self.visit(ast.lhs, Access(c.frame, c.sym, True, False ))
        #print(typeExpr)
        #print(reslhs)
        if type(typelhs) == FloatType and type(typeExpr) == IntType:
            str_I2f = self.emit.emitI2F(frame)
        self.emit.printout(resExpr + str_I2f + reslhs)

    def visitIf(self, ast, c): # 
        ctxt = c
        frame = ctxt.frame
        nenv = ctxt.sym
        #Code for expr
        expr, typeD = self.visit(ast.expr, Access(frame, nenv, False, False))
       
        #Get 2 new lables
        falseLabel = frame.getNewLabel()
        trueLabel = frame.getNewLabel()
        #Code "ifeq" + falseLabel
        self.emit.printout(expr + self.emit.emitIFFALSE(falseLabel, frame))
        #Code for "then" stmt
        for i in ast.thenStmt:
            self.visit(i, SubBody(frame, nenv))
        
        #visitStmt(ast.thenStmt, frame, nenv)

        #code "goto" + trueLabel
        self.emit.printout(self.emit.emitGOTO(str(trueLabel), frame) + self.emit.emitLABEL(falseLabel, frame))

        #code for "else" stmt
        if (ast.elseStmt != None): 
            for x in ast.elseStmt:
                self.visit(x, SubBody(frame, nenv))
           # visitStmt(ast.elseStmt.get, frame, nenv)

        #Code "trueLabel"
        self.emit.printout(self.emit.emitLABEL(trueLabel, frame))
    # def visitFor(self, ast, c):
    
    def visitContinue(self, ast, c):
        self.emit.printout(self.emit.emitLABEL(c.frame.getContinueLabel(), c.frame))
    
    def visitBreak(self, ast, c):
        self.emit.printout(self.emit.emitLABEL(c.frame.getBreakLabel(), c.frame))
    
    def visitReturn(self, ast, c):
        if ast.expr:
            (resExp,resType) = self.visit(ast.expr, Access(c.frame, c.sym, False, True))
            typeFun =  self.curFunc.mtype.rettype
            if type(typeFun) is FloatType and type(resType) is IntType:
                self.emit.printout(resExp+ self.emit.emitI2F(c.frame))
            else:
                self.emit.printout(resExp)
        self.emit.printout(self.emit.emitGOTO(c.frame.getEndLabel(),c.frame))
    def visitWhile(self, ast, c): # 
        frame = c.frame
        nenv = c.sym
        # enter loop
        frame.enterLoop()
        breakLabel = frame.getBreakLabel()
        continueLabel = frame.getContinueLabel()
        # code for continueLabel
        self.emit.printout(self.emit.emitLABEL(continueLabel, frame))
        expr, typeD = self.visit(ast.exp, Access(frame, nenv, False, True))
        #print(expr)
        #print(typeD)
        self.emit.printout(expr+ self.emit.emitIFFALSE(breakLabel, frame))

        for x in ast.sl:
            self.visit(x, SubBody(frame, nenv))
            
        self.emit.printout(self.emit.emitGOTO(continueLabel, frame))
        self.emit.printout(self.emit.emitLABEL(breakLabel, frame))
        frame.exitLoop()
    def visitCallStmt(self, ast, o):
        self.callStmtAndExp(ast, o)
        
    def visitCallExpr(self, ast, o):
        self.callStmtAndExp(ast, o)

    def callStmtAndExp(self, ast, o):
        #ast: CallStmt
        #o: Any

        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = self.lookup(ast.method.name, nenv, lambda x: x.name)
        cname = sym.value.value
    
        ctype = sym.mtype
        partype = sym.mtype.partype
        #print(ctype)
        #print(cname)
        #print((sym.name))
       # print(frame)
        in_ = ("", list())
        for x in range(len(ast.param)):
            str1, typ1 = self.visit(ast.param[x], Access(frame, nenv, False, True))
            in_ = (in_[0] + str1, in_[1].append(typ1))
            if type(partype[x]) is FloatType and type(typ1) is IntType:
                in_ = (in_[0] + self.emit.emitI2F(frame), in_[1])
        if type(ast) is CallStmt:
            self.emit.printout(in_[0])
            self.emit.printout(self.emit.emitINVOKESTATIC(cname + "/" + ast.method.name, ctype, frame))
        else:
            return in_[0] + self.emit.emitINVOKESTATIC(cname + "/" + ast.method.name, ctype, frame)
    
    def visitIntLiteral(self, ast, o):
        #ast: IntLiteral
        #o: Any
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(ast.value, frame), IntType()
    
    def visitFloatLiteral(self, ast, o):
        ctxt = o;
        frame = ctxt.frame
        return self.emit.emitPUSHFCONST(str(ast.value), frame), FloatType()

    def visitBooleanLiteral(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(str(ast.value), frame), BoolType()
    
    def visitStringLiteral(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHCONST(ast.value, StringType(), frame), StringType()

    def visitId(self, ast, c):
        sym = self.lookup(ast.name, c.sym, lambda x: x.name)
        if c.isLeft:
            if type(sym.value) is CName:
                return self.emit.emitPUTSTATIC(self.className +'.'+sym.name, sym.mtype, c.frame), sym.mtype
            else:
                return self.emit.emitWRITEVAR(sym.name, sym.mtype, sym.value.value , c.frame), sym.mtype
        else:
            
            if type(sym.value) is CName:
                return self.emit.emitGETSTATIC(self.className +'.'+sym.name, sym.mtype, c.frame), sym.mtype
            else:
                return self.emit.emitREADVAR(sym.name, sym.mtype, sym.value.value , c.frame), sym.mtype

   
    def checkEqual(self, lt, rt):
        if type(lt) == type(rt):
            return True
        else:
            return False

    def visitUnaryOp(self, ast, o):
        lc, lt= self.visit(ast.body,Access(o.frame, o.sym, False, True))
        if ast.op == '-':
            return lc + self.emit.emitNEGOP(lt, o.frame), lt
        elif ast.op == 'not':
            return lc + self.emit.emitNOT(lt, o.frame), lt

    def visitBinaryOp(self, ast, o):
        ctxt = o;
        frame = ctxt.frame
        lc, lt= self.visit(ast.left, Access(frame, o.sym, False, True))
        rc, rt= self.visit(ast.right, Access(frame, o.sym, False, True))
       # print(lc)
        #print(rc) a(ifl)+b(int) 
        if ast.op in ['+', '-']:
            if self.checkEqual(lt, rt):
                return lc + rc + self.emit.emitADDOP(ast.op, lt, frame), lt
            else:
                if type(lt) is FloatType and type(rt) is IntType:
                    return lc + rc + self.emit.emitI2F(frame)+ self.emit.emitADDOP(ast.op, lt, frame), lt
                else:
                    return lc + self.emit.emitI2F(frame) + rc + self.emit.emitADDOP(ast.op, rt, frame), rt
        elif ast.op  == '*':
            if self.checkEqual(lt, rt):
                return lc + rc + self.emit.emitMULOP(ast.op, lt, frame), lt
            else:
                if type(lt) is FloatType and type(rt) is IntType:
                    return lc + rc + self.emit.emitI2F(frame)+ self.emit.emitMULOP(ast.op, lt, frame), lt
                else:
                    return lc + self.emit.emitI2F(frame) + rc + self.emit.emitMULOP(ast.op, rt, frame), rt
        elif ast.op  == '/':
            if self.checkEqual(lt, rt):
                if type(lt) is IntType:
                    return lc + self.emit.emitI2F(frame) + rc + self.emit.emitI2F(frame) + self.emit.emitMULOP(ast.op, FloatType, frame), FloatType()
                return lc + rc + self.emit.emitMULOP(ast.op, lt, frame), lt
            else:
                if type(lt) is FloatType and type(rt) is IntType:
                    return lc + rc + self.emit.emitI2F(frame)+ self.emit.emitMULOP(ast.op, lt, frame), lt
                else:
                    return lc + self.emit.emitI2F(frame) + rc + self.emit.emitMULOP(ast.op, rt, frame), rt
        elif ast.op == 'div':
            return lc + rc + self.emit.emitDIV(frame), lt    
        elif ast.op == 'mod':
            return lc + rc + self.emit.emitMOD(frame), lt 
        elif ast.op == 'and':
            return lc + rc + self.emit.emitANDOP(frame), BoolType()
        elif ast.op == 'or':
            return lc + rc + self.emit.emitOROP(frame), BoolType() 
        elif ast.op in ['<', '<=', '>', '>=', '<>', '=']:
            if type(lt) is FloatType and type(rt) is IntType:
                return lc + rc + self.emit.emitI2F(frame)+ self.emit.emitREOP(ast.op, FloatType(), frame), BoolType()
            elif type(lt) is IntType and type(rt) is FloatType:
                return lc + self.emit.emitI2F(frame) + rc+ self.emit.emitREOP(ast.op, FloatType(), frame), BoolType()
            else:
                return lc + rc+ self.emit.emitREOP(ast.op, lt, frame), BoolType()
        
            
            
            
            