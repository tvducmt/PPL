from MPVisitor import MPVisitor
from MPParser import MPParser
from AST import *

class ASTGeneration(MPVisitor):
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return Program([self.visit(x) for x in ctx.decl()])

    def visitFuncdecl(self,ctx:MPParser.FuncdeclContext):
        local,cpstmt = self.visit(ctx.body()) 
        return FuncDecl(Id(ctx.ID().getText()),
                        [],
                        local,
                        cpstmt,
                        self.visit(ctx.mtype()))

    def visitProcdecl(self,ctx:MPParser.ProcdeclContext):
        local,cpstmt = self.visit(ctx.body()) 
        return FuncDecl(Id(ctx.ID().getText()),
                        [],
                        local,
                        cpstmt)

    def visitBody(self,ctx:MPParser.BodyContext):
        return [],[self.visit(ctx.stmt())] if ctx.stmt() else []
  
    def visitStmt(self,ctx:MPParser.StmtContext):
        return self.visit(ctx.funcall())

    def visitFuncall(self,ctx:MPParser.FuncallContext):
        return CallStmt(Id(ctx.ID().getText()),[self.visit(ctx.exp())] if ctx.exp() else [])

    def visitExp(self,ctx:MPParser.ExpContext):
        return IntLiteral(int(ctx.INTLIT().getText()))

    def visitMtype(self,ctx:MPParser.MtypeContext):
        return IntType()
        

# def test_int_literal(self):
#         input = Program([
#     		FuncDecl(Id("main"),[],[],[
#     			CallStmt(Id("putInt"),[IntLiteral(5)])])])
#         expect = "5"
#         self.assertTrue(TestCodeGen.test(input,expect,500))

#     def test_string_literal(self):
#         input = Program([
#     		FuncDecl(Id("main"),[],[],[
#     			CallStmt(Id("putString"),[StringLiteral("duc")])])])
#         expect = "duc"
#         self.assertTrue(TestCodeGen.test(input,expect,501))
#     def test_float_literal(self):
#         input = Program([
#     		FuncDecl(Id("main"),[],[],[
#     			CallStmt(Id("putFloat"),[FloatLiteral(5.5)])])])
#         expect = "5.5"
#         self.assertTrue(TestCodeGen.test(input,expect,502))

#     def test_bool_literal(self):
#         input = Program([
# 			FuncDecl(Id("main"),[],[],[
# 				CallStmt(Id("putBool"), [BooleanLiteral(True)])
# 			])
# 		])
#         expect= "true"
#         self.assertTrue(TestCodeGen.test(input,expect,503))

#     def test_assign_1(self):
#     	input = Program([
#             VarDecl(Id('a'),IntType()),
#             VarDecl(Id('b'),FloatType()),
#             FuncDecl(Id('main'),[],[],[Assign(Id('a'),IntLiteral(5)),CallStmt(Id('putInt'),[Id('a')])])
#             ])
#     	expect = "5"
#     	self.assertTrue(TestCodeGen.test(input,expect,504))
#     def test_assign_2(self):
#         input = Program([
#             VarDecl(Id('a'),IntType()),
#             VarDecl(Id('b'),FloatType()),
#             FuncDecl(Id('main'),[],[],[Assign(Id('a'),IntLiteral(5)),CallStmt(Id('putFloat'),[Id('a')])])
#             ])
#         expect = "5.0"
#         self.assertTrue(TestCodeGen.test(input,expect,505))
    
#     def test_assign_3(self):
#         input = Program([
#             VarDecl(Id('a'),IntType()),
#             VarDecl(Id('b'),FloatType()),
#             FuncDecl(Id('main'),[],[],[Assign(Id('b'),IntLiteral(5)),CallStmt(Id('putFloat'),[Id('b')])])
#             ])
#         expect = "5.0"
#         self.assertTrue(TestCodeGen.test(input,expect,505))
    
#     def test_assign_4(self):
#         input = Program([
#             VarDecl(Id('a'),IntType()),
#             VarDecl(Id('b'),BoolType()),
#             FuncDecl(Id('main'),[],[],[Assign(Id('b'),BooleanLiteral('True')),CallStmt(Id('putBool'),[Id('b')])])
#             ])
#         expect = "true"
#         self.assertTrue(TestCodeGen.test(input,expect,505))
    
#     def test_assign_multi_1(self):
#         input = Program([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),IntType()),VarDecl(Id('c'),IntType()),
#         VarDecl(Id('d'),FloatType()),
#         FuncDecl(Id('main'),[],[],[Assign(Id('c'),IntLiteral(5)),Assign(Id('b'),Id('c')),
#         Assign(Id('a'),Id('b')),
#         CallStmt(Id('putInt'),[Id('c')]),CallStmt(Id('putInt'),[Id('a')])])])
#         expect = "55"
#         self.assertTrue(TestCodeGen.test(input,expect,505))
#     def test_assign_multi_2(self):
#         input = Program([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),IntType()),VarDecl(Id('c'),IntType()),
#         VarDecl(Id('d'),FloatType()),
#         FuncDecl(Id('main'),[],[],[Assign(Id('c'),IntLiteral(5)),Assign(Id('b'),Id('c')),
#         Assign(Id('d'),Id('b')),
#         CallStmt(Id('putInt'),[Id('c')]),CallStmt(Id('putFloat'),[Id('d')])])])
#         expect = "55.0"
#         self.assertTrue(TestCodeGen.test(input,expect,506))
#     def test_binary_add_1(self):
#         input = Program([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),IntType()),VarDecl(Id('c'),IntType()),
#         VarDecl(Id('d'),FloatType()),
#         FuncDecl(Id('main'),[],[],[Assign(Id('c'),IntLiteral(5)),Assign(Id('b'),Id('c')),
#         Assign(Id('d'),Id('b')),
#         CallStmt(Id('putInt'),[BinaryOp( '+', IntLiteral(1),IntLiteral(1)),])])])
#         expect = "2"
#         self.assertTrue(TestCodeGen.test(input,expect,507))
#     def test_binary_add_2(self):
#         input = Program([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),IntType()),VarDecl(Id('c'),IntType()),
#         VarDecl(Id('d'),FloatType()),
#         FuncDecl(Id('main'),[],[],[Assign(Id('c'),IntLiteral(5)),Assign(Id('b'),Id('c')),
#         Assign(Id('d'),Id('b')),
#         CallStmt(Id('putFloat'),[BinaryOp( '+', FloatLiteral(1.0),IntLiteral(1)),])])])
#         expect = "2.0"
#         self.assertTrue(TestCodeGen.test(input,expect,507))
#     def test_binary_mul_1(self):
#         input = Program([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),IntType()),VarDecl(Id('c'),IntType()),
#         VarDecl(Id('d'),FloatType()),
#         FuncDecl(Id('main'),[],[],[
#         CallStmt(Id('putFloat'),[BinaryOp( '*', FloatLiteral(2.5),IntLiteral(2)),])])])
#         expect = "5.0"
#         self.assertTrue(TestCodeGen.test(input,expect,508))
#     def test_binary_mul_2(self):
#         input = Program([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),IntType()),VarDecl(Id('c'),IntType()),
#         VarDecl(Id('d'),FloatType()),
#         FuncDecl(Id('main'),[],[],[
#         CallStmt(Id('putFloat'),[BinaryOp( '/', IntLiteral(4),IntLiteral(2)),])])])
#         expect = "2.0"
#         self.assertTrue(TestCodeGen.test(input,expect,509))
#     def test_binary_mul_3(self):
#         input = Program([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),IntType()),VarDecl(Id('c'),IntType()),
#         VarDecl(Id('d'),FloatType()),
#         FuncDecl(Id('main'),[],[],[
#         CallStmt(Id('putFloat'),[BinaryOp( '/', FloatLiteral(4.0),FloatLiteral(2.0)),])])])
#         expect = "2.0"
#         self.assertTrue(TestCodeGen.test(input,expect,510))
#     def test_binary_mul_4(self):
#         input = Program([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),IntType()),VarDecl(Id('c'),IntType()),
#         VarDecl(Id('d'),FloatType()),
#         FuncDecl(Id('main'),[],[],[
#         CallStmt(Id('putFloat'),[BinaryOp( '/', IntLiteral(4),FloatLiteral(2.0)),])])])
#         expect = "2.0"
#         self.assertTrue(TestCodeGen.test(input,expect,511))
#     def test_binary_mul_add_2(self):
#         input = Program([
#         FuncDecl(Id('main'),[],[],[
#         CallStmt(Id('putFloat'),[BinaryOp('+',BinaryOp('-',BinaryOp('/',BinaryOp('*',IntLiteral(10),IntLiteral(3)),IntLiteral(2)),IntLiteral(10)),IntLiteral(5))])])])
#         expect = "10.0"
#         self.assertTrue(TestCodeGen.test(input,expect,512))
#     def test_binary_mul_add_1(self):
#         input = Program([
#         FuncDecl(Id('main'),[],[],[
#         CallStmt(Id('putFloat'),[BinaryOp('-',BinaryOp('*',IntLiteral(11),IntLiteral(2)),BinaryOp('/',IntLiteral(10),IntLiteral(2)))])])])
#         expect = "17.0"
#         self.assertTrue(TestCodeGen.test(input,expect,513))
#     def test_binary_mod_1(self):
#         input = Program([
#         FuncDecl(Id('main'),[],[VarDecl(Id('a'),IntType())],[
#             Assign(Id('a'),IntLiteral(5)),
#         CallStmt(Id('putInt'),[BinaryOp('mod',IntLiteral(5), IntLiteral(2))])])])
#         expect = "1"
#         self.assertTrue(TestCodeGen.test(input,expect,514))
#     def test_binary_mod_2(self):
#         input = Program([
#         FuncDecl(Id('main'),[],[VarDecl(Id('a'),IntType()), VarDecl(Id('b'),IntType())],[
#             Assign(Id('a'),IntLiteral(5)),
#             Assign(Id('b'),IntLiteral(3)),
#         CallStmt(Id('putInt'),[BinaryOp('mod',BinaryOp('+', Id('a'), IntLiteral(15)), BinaryOp('+', Id('b'), IntLiteral(4)))])])])
#         expect = "6"
#         self.assertTrue(TestCodeGen.test(input,expect,515))
#     def test_binary_div_1(self):
#         input = Program([
#         FuncDecl(Id('main'),[],[VarDecl(Id('a'),IntType())],[
#             Assign(Id('a'),IntLiteral(5)),
#         CallStmt(Id('putInt'),[BinaryOp('div',IntLiteral(5), IntLiteral(2))])])])
#         expect = "2"
#         self.assertTrue(TestCodeGen.test(input,expect,516))
#     def test_binary_div_2(self):
#         input = Program([
#         FuncDecl(Id('main'),[],[VarDecl(Id('a'),IntType()), VarDecl(Id('b'),IntType())],[
#             Assign(Id('a'),IntLiteral(5)),
#             Assign(Id('b'),IntLiteral(3)),
#         CallStmt(Id('putInt'),[BinaryOp('div',BinaryOp('+', Id('a'), IntLiteral(15)), BinaryOp('+', Id('b'), IntLiteral(4)))])])])
#         expect = "2"
#         self.assertTrue(TestCodeGen.test(input,expect,517))
#     def test_binary_div_3(self):
#         input = Program([
#         FuncDecl(Id('main'),[],[VarDecl(Id('a'),IntType()), VarDecl(Id('b'),IntType())],[
#             Assign(Id('a'),IntLiteral(99)),
#             Assign(Id('b'),IntLiteral(3)),
#         CallStmt(Id('putInt'),[BinaryOp('div',BinaryOp('mod',Id('a'),IntLiteral(15)),BinaryOp('+',Id('b'),IntLiteral(4)))])])])
#         expect = "1"
#         self.assertTrue(TestCodeGen.test(input,expect,518))
#     def test_binary_div_4(self):
#         input = Program([
#         FuncDecl(Id('main'),[],[VarDecl(Id('a'),IntType()), VarDecl(Id('b'),IntType())],[
#             Assign(Id('a'),IntLiteral(49)),
#             Assign(Id('b'),IntLiteral(3)),
#         CallStmt(Id('putInt'),[BinaryOp('+',BinaryOp('mod',BinaryOp('*',Id('a'),IntLiteral(2)),IntLiteral(15)),BinaryOp('div',IntLiteral(15),BinaryOp('+',Id('b'),IntLiteral(4))))])])])
#         expect = "10"
#         self.assertTrue(TestCodeGen.test(input,expect,519))
#     def test_binary_andor_1(self):
#         input = Program([VarDecl(Id('a'),IntType()),
#         VarDecl(Id('b'),IntType()),
#         VarDecl(Id('c'),IntType()),
#         VarDecl(Id('d'),BoolType()),
#         FuncDecl(Id('main'),[],[],
#         [Assign(Id('d'),BooleanLiteral(True)),
#         Assign(Id('b'),IntLiteral(3)),
#         CallStmt(Id('putBool'),[BinaryOp('and',BooleanLiteral(True),BooleanLiteral(True))])])])
#         expect = "true"
#         self.assertTrue(TestCodeGen.test(input,expect,520))
#     def test_binary_andor_2(self):
#         input = Program([VarDecl(Id('a'),IntType()),
#         VarDecl(Id('b'),IntType()),
#         VarDecl(Id('c'),IntType()),
#         VarDecl(Id('d'),BoolType()),
#         FuncDecl(Id('main'),[],[],
#         [Assign(Id('d'),BooleanLiteral(False)),
#         Assign(Id('b'),IntLiteral(3)),
#         CallStmt(Id('putBool'),[BinaryOp('and',BooleanLiteral(True),Id('d'))])])])
#         expect = "false"
#         self.assertTrue(TestCodeGen.test(input,expect,521))
#     def test_binary_andor_3(self):
#         input = Program([VarDecl(Id('a'),IntType()),
#         VarDecl(Id('b'),IntType()),
#         VarDecl(Id('c'),IntType()),
#         VarDecl(Id('d'),BoolType()),
#         FuncDecl(Id('main'),[],[],
#         [Assign(Id('d'),BooleanLiteral(False)),
#         Assign(Id('b'),IntLiteral(3)),
#         CallStmt(Id('putBool'),[BinaryOp('and',BooleanLiteral(True),BinaryOp('and', BooleanLiteral(False), Id('d')))])])])
#         expect = "false"
#         self.assertTrue(TestCodeGen.test(input,expect,522))
#     def test_binary_andor_4(self):
#         input = Program([VarDecl(Id('a'),IntType()),
       
#         FuncDecl(Id('main'),[],[],
#         [
#         CallStmt(Id('putBool'),[BinaryOp('or',BooleanLiteral(True),BinaryOp('and', BooleanLiteral(False), BooleanLiteral(False)))])])])
#         expect = "true"
#         self.assertTrue(TestCodeGen.test(input,expect,523))
#     def test_binary_andor_5(self):
#         input = Program([VarDecl(Id('a'),IntType()),
       
#         FuncDecl(Id('main'),[],[],
#         [
#         CallStmt(Id('putBool'),[BinaryOp('and',BooleanLiteral(True),BinaryOp('or', BooleanLiteral(False), BooleanLiteral(False)))])])])
#         expect = "false"
#         self.assertTrue(TestCodeGen.test(input,expect,524))
#     def test_relation_expression_6(self):
#         input = Program([VarDecl(Id('a'),IntType()),
#         VarDecl(Id('b'),IntType()),
#         VarDecl(Id('c'),IntType()),
#         VarDecl(Id('d'),BoolType()),
#         FuncDecl(Id('main'),[],[],
#         [Assign(Id('a'),IntLiteral(5)),
#         Assign(Id('b'),IntLiteral(6)),
#         CallStmt(Id('putBool'),[BinaryOp('<>',Id('b'),BinaryOp('*', Id('a'), IntLiteral(2)))])])])
#         expect = "true"
#         self.assertTrue(TestCodeGen.test(input,expect,525))

#     def test_relation_expression_9(self):
#         input = Program([VarDecl(Id('a'),IntType()),
#         VarDecl(Id('b'),IntType()),
#         VarDecl(Id('c'),IntType()),
#         VarDecl(Id('d'),BoolType()),
#         FuncDecl(Id('main'),[],[],
#         [Assign(Id('a'),IntLiteral(5)),
#         Assign(Id('b'),IntLiteral(10)),
#         CallStmt(Id('putBool'),[BinaryOp('=',BinaryOp('mod',Id('b'),IntLiteral(2)),IntLiteral(0))])])])
#         expect = "true"
#         self.assertTrue(TestCodeGen.test(input,expect,526))
#     def test_relation_expression_10(self):
#         input = Program([VarDecl(Id('a'),IntType()),
#         VarDecl(Id('b'),IntType()),
#         VarDecl(Id('c'),IntType()),
#         VarDecl(Id('d'),BoolType()),
#         FuncDecl(Id('main'),[],[],
#         [Assign(Id('a'),IntLiteral(5)),
#         Assign(Id('b'),IntLiteral(10)),
#         CallStmt(Id('putBool'),[BinaryOp('or',BinaryOp('>',Id('a'),Id('b')),BinaryOp('and',BinaryOp('=',BinaryOp('mod',Id('b'),IntLiteral(2)),IntLiteral(0)),BinaryOp('>',BinaryOp('*',Id('b'),IntLiteral(2)),IntLiteral(18))))])])])
#         expect = "true"
#         self.assertTrue(TestCodeGen.test(input,expect,527))
#     def test_unaryOp_1(self):
#         input = Program([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),FloatType()),FuncDecl(Id('main'),[],[],
#         [Assign(Id('a'),IntLiteral(5)),
#         CallStmt(Id('putInt'),[UnaryOp('-',Id('a'))])])
#         ])
#         expect = "-5"
#         self.assertTrue(TestCodeGen.test(input,expect,528))
#     def test_unaryOp_2(self):
#         input = Program([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),FloatType()),FuncDecl(Id('main'),[],[],
#         [Assign(Id('b'),FloatLiteral(5.5)),
#         CallStmt(Id('putFloat'),[UnaryOp('-',UnaryOp('-',UnaryOp('-',Id('b'))))])])
#         ])
#         expect = "-5.5"
#         self.assertTrue(TestCodeGen.test(input,expect,529))
#     def test_unaryOp_3(self):
#         input = Program([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),BoolType()),FuncDecl(Id('main'),[],[],
#         [Assign(Id('b'),BooleanLiteral(True)),
#         CallStmt(Id('putBool'),[UnaryOp('not', Id('b'))])])
#         ])
#         expect = "false"
#         self.assertTrue(TestCodeGen.test(input,expect,530))
    
#     def test_relation_expression_9(self):
#         input = Program([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),IntType()),
#         FuncDecl(Id('main'),[],[],[
#             Assign(Id('a'),IntLiteral(5)),Assign(Id('b'),IntLiteral(10)),
#             CallStmt(Id('putBool'),[BinaryOp('or',BinaryOp('<=',BinaryOp('+',Id('a'),IntLiteral(1)),BinaryOp('div',Id('b'),IntLiteral(2))),BinaryOp('=',BinaryOp('mod',Id('b'),IntLiteral(2)),IntLiteral(0)))])])
#         ])
#         expect = "true"
#         self.assertTrue(TestCodeGen.test(input,expect,531))
#     def test_relation_expression_10(self):
#         input = Program([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),IntType()),
#         FuncDecl(Id('main'),[],[],[
#             Assign(Id('a'),IntLiteral(5)),Assign(Id('b'),IntLiteral(10)),
#             CallStmt(Id('putBool'),[BinaryOp('or',BinaryOp('>',Id('a'),Id('b')),BinaryOp('and',BinaryOp('=',BinaryOp('mod',Id('b'),IntLiteral(2)),IntLiteral(0)),BinaryOp('>',BinaryOp('*',Id('b'),IntLiteral(2)),IntLiteral(18))))])])
#         ])
#         expect = "true"
#         self.assertTrue(TestCodeGen.test(input,expect,532))
#     def test_unaryOp_4(self):
#         input = Program([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),BoolType()),FuncDecl(Id('main'),[],[],
#         [Assign(Id('b'),BooleanLiteral(True)),
#         CallStmt(Id('putBool'),[UnaryOp('not',UnaryOp('not',BinaryOp('<>',Id('a'),IntLiteral(8))))])])
#         ])
#         expect = "false"
#         self.assertTrue(TestCodeGen.test(input,expect,533))
# # def test_local_declare_1(self):
# #         input = Program([
# #             VarDecl(Id('a'),IntType()),
# #             VarDecl(Id('b'),IntType()),
# #             VarDecl(Id('c'),FloatType()),
# #             VarDecl(Id('d'),FloatType()),
# #             FuncDecl(Id('main'),[],[],
# #                 [CallStmt(Id('putFloat'),[CallExpr(Id('foo'),[Id('c')])])]),
# #             FuncDecl(Id('foo'),[VarDecl(Id('a'),FloatType())],[VarDecl(Id('x'),BoolType()),VarDecl(Id('y'),BoolType())],[Assign(Id('a'),FloatLiteral(2.5)),Return((Id('a')))], FloatType()),VarDecl(Id('e'),BoolType()),VarDecl(Id('f'),BoolType()),VarDecl(Id('g'),StringType()),VarDecl(Id('h'),StringType())
# #             ])
# #         expect = "2.5"
# #         self.assertTrue(TestCodeGen.test(input,expect,534))
#     def test_short_circuit_1(self):
#         input = Program([
            
#             FuncDecl(Id('main'),[],[VarDecl(Id('a'),IntType()),VarDecl(Id('b'),IntType())],
#             [
#                 Assign(Id('a'),IntLiteral(5)),
#                 If(BinaryOp('andthen',BooleanLiteral(True),BinaryOp('>=',Id('a'),IntLiteral(9))),
#                 [CallStmt(Id('putInt'),[Id('a')])],[CallStmt(Id('putInt'),[IntLiteral(2)])])
#             ])
#             ])
#         expect = "2"
#         self.assertTrue(TestCodeGen.test(input,expect,535))

#     def test_short_circuit_2(self):
#         input = Program([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),BoolType()),FuncDecl(Id('main'),[],[],[Assign(Id('a'),IntLiteral(5)),If(BinaryOp('andthen',BinaryOp('andthen',BooleanLiteral(True),BinaryOp('<=',Id('a'),IntLiteral(1))),BinaryOp('<>',Id('a'),IntLiteral(4))),[CallStmt(Id('putInt'),[Id('a')])],[CallStmt(Id('putInt'),[IntLiteral(2)])])])]) 
#         expect = "2"
#         self.assertTrue(TestCodeGen.test(input,expect,536))
#     def test_short_circuit_3(self):
#         input = Program([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),BoolType()),FuncDecl(Id('main'),[],[],[Assign(Id('a'),IntLiteral(5)),If(BinaryOp('orelse',BinaryOp('orelse',BinaryOp('>',Id('a'),IntLiteral(5)),BooleanLiteral(True)),BinaryOp('>',Id('a'),IntLiteral(10))),[CallStmt(Id('putInt'),[Id('a')])],[CallStmt(Id('putInt'),[IntLiteral(2)])])])]) 
#         expect = "2"
#         self.assertTrue(TestCodeGen.test(input,expect,537))

#     def test_if_statement_1(self):
#         input = Program([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),FloatType()),FuncDecl(Id('main'),[],[],[If(BinaryOp('>',IntLiteral(3),IntLiteral(1)),[Assign(Id('a'),IntLiteral(2)),CallStmt(Id('putInt'),[Id('a')])],[CallStmt(Id('putInt'),[IntLiteral(5)])])])])
#         expect = "2"
#         self.assertTrue(TestCodeGen.test(input,expect,538))
#     def test_if_statement_2(self):
#         input = Program([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),FloatType()),FuncDecl(Id('main'),[],[],[Assign(Id('a'),IntLiteral(11)), If(BinaryOp('>',IntLiteral(3),IntLiteral(1)),[CallStmt(Id('putInt'),[Id('a')]),If(BinaryOp('=',BinaryOp('+',Id('a'),IntLiteral(1)),IntLiteral(15)),[CallStmt(Id('putString'),[StringLiteral('kien')])],[CallStmt(Id('putString'),[StringLiteral('no kien')])])],[]),CallStmt(Id('putInt'),[IntLiteral(5)])])])
#         expect = "11no kien5"
#         self.assertTrue(TestCodeGen.test(input,expect,539))
#  ##-------- test test_while_statement
 
#     def test_while_statement_1(self):
#         input = Program([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),FloatType()),FuncDecl(Id('main'),[],[],[Assign(Id('a'),IntLiteral(4)),While(BinaryOp('>',Id('a'),IntLiteral(1)),[CallStmt(Id('putInt'),[Id('a')]),Assign(Id('a'),BinaryOp('-',Id('a'),IntLiteral(1)))])])])
#         expect = "432"
#         self.assertTrue(TestCodeGen.test(input,expect,540))
#     def test_while_statement_2(self):
#         input = Program([VarDecl(Id('a'),IntType()), VarDecl(Id('c'),IntType()), VarDecl(Id('b'),FloatType()),FuncDecl(Id('main'),[],[],[Assign(Id('a'),IntLiteral(20)),Assign(Id('c'),IntLiteral(2)),While(BinaryOp('>',Id('a'),IntLiteral(1)),[CallStmt(Id('putInt'),[Id('a')]),Assign(Id('a'),BinaryOp('-',Id('a'),IntLiteral(3))),While(BinaryOp('<',Id('c'),IntLiteral(10)),[CallStmt(Id('putInt'),[Id('c')]),Assign(Id('c'),BinaryOp('+',Id('c'),IntLiteral(1)))])])])])
#         expect = "2023456789171411852"
#         self.assertTrue(TestCodeGen.test(input,expect,541))

#     def test_with_statement_1(self):
#         input = Program([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),FloatType()),FuncDecl(Id('main'),[],[],[With([VarDecl(Id('a'),FloatType())],[Assign(Id('a'),FloatLiteral(1.1)),CallStmt(Id('putFloat'),[Id('a')])]),With([VarDecl(Id('f'),BoolType())],[Assign(Id('f'),BooleanLiteral(True)),CallStmt(Id('putBool'),[Id('f')])])])])
#         expect = "1.1true"
#         self.assertTrue(TestCodeGen.test(input,expect,542))
    
#     def test_multi_statement_1(self):
#         input = Program([VarDecl(Id('a'),IntType()),VarDecl(Id('c'),IntType()),VarDecl(Id('b'),IntType()),VarDecl(Id('e'),FloatType()),VarDecl(Id('d'),BoolType()),FuncDecl(Id('main'),[],[],[Assign(Id('b'),IntLiteral(5)),Assign(Id('c'),IntLiteral(2)),With([VarDecl(Id('a'),BoolType())],[Assign(Id('a'),BinaryOp('>',Id('c'),IntLiteral(3))),If(BinaryOp('or',Id('a'),BooleanLiteral(True)),[While(BinaryOp('<',Id('b'),IntLiteral(15)),[CallStmt(Id('putInt'),[Id('b')]),Assign(Id('b'),BinaryOp('+',Id('b'),IntLiteral(3)))])],[])])])])
#         expect = "581114"
#         self.assertTrue(TestCodeGen.test(input,expect,543))
#     def test_for_statement_2(self):
#         input = Program([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),FloatType()),FuncDecl(Id('main'),[],[],[For(Id('a'),IntLiteral(1),IntLiteral(5),True,[CallStmt(Id('putInt'),[Id('a')])])])])
#         expect = "12345"
#         self.assertTrue(TestCodeGen.test(input,expect,544))
