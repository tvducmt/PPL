import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    # def test_int_literal(self):
    #     input = Program([
    # 		FuncDecl(Id("main"),[],[],[
    # 			CallStmt(Id("putInt"),[IntLiteral(5)])])])
    #     expect = "5"
    #     self.assertTrue(TestCodeGen.test(input,expect,500))

    # def test_string_literal(self):
    #     input = Program([
    # 		FuncDecl(Id("main"),[],[],[
    # 			CallStmt(Id("putString"),[StringLiteral("duc")])])])
    #     expect = "duc"
    #     self.assertTrue(TestCodeGen.test(input,expect,501))
    # def test_float_literal(self):
    #     input = Program([
    # 		FuncDecl(Id("main"),[],[],[
    # 			CallStmt(Id("putFloat"),[FloatLiteral(5.5)])])])
    #     expect = "5.5"
    #     self.assertTrue(TestCodeGen.test(input,expect,502))

    # def test_bool_literal(self):
    #     input = Program([
	# 		FuncDecl(Id("main"),[],[],[
	# 			CallStmt(Id("putBool"), [BooleanLiteral(True)])
	# 		])
	# 	])
    #     expect= "true"
    #     self.assertTrue(TestCodeGen.test(input,expect,503))

    # def test_assign_1(self):
    # 	input = Program([
    #         VarDecl(Id('a'),IntType()),
    #         VarDecl(Id('b'),FloatType()),
    #         FuncDecl(Id('main'),[],[],[Assign(Id('a'),IntLiteral(5)),CallStmt(Id('putInt'),[Id('a')])])
    #         ])
    # 	expect = "5"
    # 	self.assertTrue(TestCodeGen.test(input,expect,504))
    # def test_assign_2(self):
    #     input = Program([
    #         VarDecl(Id('a'),IntType()),
    #         VarDecl(Id('b'),FloatType()),
    #         FuncDecl(Id('main'),[],[],[Assign(Id('a'),IntLiteral(5)),CallStmt(Id('putFloat'),[Id('a')])])
    #         ])
    #     expect = "5.0"
    #     self.assertTrue(TestCodeGen.test(input,expect,505))
    
    # def test_assign_3(self):
    #     input = Program([
    #         VarDecl(Id('a'),IntType()),
    #         VarDecl(Id('b'),FloatType()),
    #         FuncDecl(Id('main'),[],[],[Assign(Id('b'),IntLiteral(5)),CallStmt(Id('putFloat'),[Id('b')])])
    #         ])
    #     expect = "5.0"
    #     self.assertTrue(TestCodeGen.test(input,expect,505))
    
    # def test_assign_4(self):
    #     input = Program([
    #         VarDecl(Id('a'),IntType()),
    #         VarDecl(Id('b'),BoolType()),
    #         FuncDecl(Id('main'),[],[],[Assign(Id('b'),BooleanLiteral('True')),CallStmt(Id('putBool'),[Id('b')])])
    #         ])
    #     expect = "true"
    #     self.assertTrue(TestCodeGen.test(input,expect,505))
    
    # def test_assign_multi_1(self):
    #     input = Program([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),IntType()),VarDecl(Id('c'),IntType()),
    #     VarDecl(Id('d'),FloatType()),
    #     FuncDecl(Id('main'),[],[],[Assign(Id('c'),IntLiteral(5)),Assign(Id('b'),Id('c')),
    #     Assign(Id('a'),Id('b')),
    #     CallStmt(Id('putInt'),[Id('c')]),CallStmt(Id('putInt'),[Id('a')])])])
    #     expect = "55"
    #     self.assertTrue(TestCodeGen.test(input,expect,505))
    # def test_assign_multi_2(self):
    #     input = Program([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),IntType()),VarDecl(Id('c'),IntType()),
    #     VarDecl(Id('d'),FloatType()),
    #     FuncDecl(Id('main'),[],[],[Assign(Id('c'),IntLiteral(5)),Assign(Id('b'),Id('c')),
    #     Assign(Id('d'),Id('b')),
    #     CallStmt(Id('putInt'),[Id('c')]),CallStmt(Id('putFloat'),[Id('d')])])])
    #     expect = "55.0"
    #     self.assertTrue(TestCodeGen.test(input,expect,506))
    # def test_binary_add_1(self):
    #     input = Program([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),IntType()),VarDecl(Id('c'),IntType()),
    #     VarDecl(Id('d'),FloatType()),
    #     FuncDecl(Id('main'),[],[],[Assign(Id('c'),IntLiteral(5)),Assign(Id('b'),Id('c')),
    #     Assign(Id('d'),Id('b')),
    #     CallStmt(Id('putInt'),[BinaryOp( '+', IntLiteral(1),IntLiteral(1)),])])])
    #     expect = "2"
    #     self.assertTrue(TestCodeGen.test(input,expect,507))
    # def test_binary_add_2(self):
    #     input = Program([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),IntType()),VarDecl(Id('c'),IntType()),
    #     VarDecl(Id('d'),FloatType()),
    #     FuncDecl(Id('main'),[],[],[Assign(Id('c'),IntLiteral(5)),Assign(Id('b'),Id('c')),
    #     Assign(Id('d'),Id('b')),
    #     CallStmt(Id('putFloat'),[BinaryOp( '+', FloatLiteral(1.0),IntLiteral(1)),])])])
    #     expect = "2.0"
    #     self.assertTrue(TestCodeGen.test(input,expect,507))
    # def test_binary_mul_1(self):
    #     input = Program([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),IntType()),VarDecl(Id('c'),IntType()),
    #     VarDecl(Id('d'),FloatType()),
    #     FuncDecl(Id('main'),[],[],[
    #     CallStmt(Id('putFloat'),[BinaryOp( '*', FloatLiteral(2.5),IntLiteral(2)),])])])
    #     expect = "5.0"
    #     self.assertTrue(TestCodeGen.test(input,expect,508))
    # def test_binary_mul_2(self):
    #     input = Program([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),IntType()),VarDecl(Id('c'),IntType()),
    #     VarDecl(Id('d'),FloatType()),
    #     FuncDecl(Id('main'),[],[],[
    #     CallStmt(Id('putFloat'),[BinaryOp( '/', IntLiteral(4),IntLiteral(2)),])])])
    #     expect = "2.0"
    #     self.assertTrue(TestCodeGen.test(input,expect,509))
    # def test_binary_mul_3(self):
    #     input = Program([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),IntType()),VarDecl(Id('c'),IntType()),
    #     VarDecl(Id('d'),FloatType()),
    #     FuncDecl(Id('main'),[],[],[
    #     CallStmt(Id('putFloat'),[BinaryOp( '/', FloatLiteral(4.0),FloatLiteral(2.0)),])])])
    #     expect = "2.0"
    #     self.assertTrue(TestCodeGen.test(input,expect,510))
    # def test_binary_mul_4(self):
    #     input = Program([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),IntType()),VarDecl(Id('c'),IntType()),
    #     VarDecl(Id('d'),FloatType()),
    #     FuncDecl(Id('main'),[],[],[
    #     CallStmt(Id('putFloat'),[BinaryOp( '/', IntLiteral(4),FloatLiteral(2.0)),])])])
    #     expect = "2.0"
    #    self.assertTrue(TestCodeGen.test(input,expect,511))
    # def test_binary_mul_add_2(self):
    #     input = Program([
    #     FuncDecl(Id('main'),[],[],[
    #     CallStmt(Id('putFloat'),[BinaryOp('+',BinaryOp('-',BinaryOp('/',BinaryOp('*',IntLiteral(10),IntLiteral(3)),IntLiteral(2)),IntLiteral(10)),IntLiteral(5))])])])
    #     expect = "10.0"
    #     self.assertTrue(TestCodeGen.test(input,expect,512))
    # def test_binary_mul_add_1(self):
    #     input = Program([
    #     FuncDecl(Id('main'),[],[],[
    #     CallStmt(Id('putFloat'),[BinaryOp('-',BinaryOp('*',IntLiteral(11),IntLiteral(2)),BinaryOp('/',IntLiteral(10),IntLiteral(2)))])])])
    #     expect = "17.0"
    #     self.assertTrue(TestCodeGen.test(input,expect,513))
    # def test_binary_mod_1(self):
    #     input = Program([
    #     FuncDecl(Id('main'),[],[VarDecl(Id('a'),IntType())],[
    #         Assign(Id('a'),IntLiteral(5)),
    #     CallStmt(Id('putInt'),[BinaryOp('mod',IntLiteral(5), IntLiteral(2))])])])
    #     expect = "1"
    #     self.assertTrue(TestCodeGen.test(input,expect,514))
    # def test_binary_mod_2(self):
    #     input = Program([
    #     FuncDecl(Id('main'),[],[VarDecl(Id('a'),IntType()), VarDecl(Id('b'),IntType())],[
    #         Assign(Id('a'),IntLiteral(5)),
    #         Assign(Id('b'),IntLiteral(3)),
    #     CallStmt(Id('putInt'),[BinaryOp('mod',BinaryOp('+', Id('a'), IntLiteral(15)), BinaryOp('+', Id('b'), IntLiteral(4)))])])])
    #     expect = "6"
    #     self.assertTrue(TestCodeGen.test(input,expect,515))
    # def test_binary_div_1(self):
    #     input = Program([
    #     FuncDecl(Id('main'),[],[VarDecl(Id('a'),IntType())],[
    #         Assign(Id('a'),IntLiteral(5)),
    #     CallStmt(Id('putInt'),[BinaryOp('div',IntLiteral(5), IntLiteral(2))])])])
    #     expect = "2"
    #     self.assertTrue(TestCodeGen.test(input,expect,516))
    # def test_binary_div_2(self):
    #     input = Program([
    #     FuncDecl(Id('main'),[],[VarDecl(Id('a'),IntType()), VarDecl(Id('b'),IntType())],[
    #         Assign(Id('a'),IntLiteral(5)),
    #         Assign(Id('b'),IntLiteral(3)),
    #     CallStmt(Id('putInt'),[BinaryOp('div',BinaryOp('+', Id('a'), IntLiteral(15)), BinaryOp('+', Id('b'), IntLiteral(4)))])])])
    #     expect = "2"
    #     self.assertTrue(TestCodeGen.test(input,expect,517))
    # def test_binary_div_3(self):
    #     input = Program([
    #     FuncDecl(Id('main'),[],[VarDecl(Id('a'),IntType()), VarDecl(Id('b'),IntType())],[
    #         Assign(Id('a'),IntLiteral(99)),
    #         Assign(Id('b'),IntLiteral(3)),
    #     CallStmt(Id('putInt'),[BinaryOp('div',BinaryOp('mod',Id('a'),IntLiteral(15)),BinaryOp('+',Id('b'),IntLiteral(4)))])])])
    #     expect = "1"
    #     self.assertTrue(TestCodeGen.test(input,expect,518))
    # def test_binary_div_4(self):
    #     input = Program([
    #     FuncDecl(Id('main'),[],[VarDecl(Id('a'),IntType()), VarDecl(Id('b'),IntType())],[
    #         Assign(Id('a'),IntLiteral(49)),
    #         Assign(Id('b'),IntLiteral(3)),
    #     CallStmt(Id('putInt'),[BinaryOp('+',BinaryOp('mod',BinaryOp('*',Id('a'),IntLiteral(2)),IntLiteral(15)),BinaryOp('div',IntLiteral(15),BinaryOp('+',Id('b'),IntLiteral(4))))])])])
    #     expect = "10"
    #     self.assertTrue(TestCodeGen.test(input,expect,519))
    # def test_binary_andor_1(self):
    #     input = Program([VarDecl(Id('a'),IntType()),
    #     VarDecl(Id('b'),IntType()),
    #     VarDecl(Id('c'),IntType()),
    #     VarDecl(Id('d'),BoolType()),
    #     FuncDecl(Id('main'),[],[],
    #     [Assign(Id('d'),BooleanLiteral(True)),
    #     Assign(Id('b'),IntLiteral(3)),
    #     CallStmt(Id('putBool'),[BinaryOp('and',BooleanLiteral(True),BooleanLiteral(True))])])])
    #     expect = "true"
    #     self.assertTrue(TestCodeGen.test(input,expect,520))
    # def test_binary_andor_2(self):
    #     input = Program([VarDecl(Id('a'),IntType()),
    #     VarDecl(Id('b'),IntType()),
    #     VarDecl(Id('c'),IntType()),
    #     VarDecl(Id('d'),BoolType()),
    #     FuncDecl(Id('main'),[],[],
    #     [Assign(Id('d'),BooleanLiteral(False)),
    #     Assign(Id('b'),IntLiteral(3)),
    #     CallStmt(Id('putBool'),[BinaryOp('and',BooleanLiteral(True),Id('d'))])])])
    #     expect = "false"
    #     self.assertTrue(TestCodeGen.test(input,expect,521))
    # def test_binary_andor_3(self):
    #     input = Program([VarDecl(Id('a'),IntType()),
    #     VarDecl(Id('b'),IntType()),
    #     VarDecl(Id('c'),IntType()),
    #     VarDecl(Id('d'),BoolType()),
    #     FuncDecl(Id('main'),[],[],
    #     [Assign(Id('d'),BooleanLiteral(False)),
    #     Assign(Id('b'),IntLiteral(3)),
    #     CallStmt(Id('putBool'),[BinaryOp('and',BooleanLiteral(True),BinaryOp('and', BooleanLiteral(False), Id('d')))])])])
    #     expect = "false"
    #     self.assertTrue(TestCodeGen.test(input,expect,522))
    # def test_binary_andor_4(self):
    #     input = Program([VarDecl(Id('a'),IntType()),
       
    #     FuncDecl(Id('main'),[],[],
    #     [
    #     CallStmt(Id('putBool'),[BinaryOp('or',BooleanLiteral(True),BinaryOp('and', BooleanLiteral(False), BooleanLiteral(False)))])])])
    #     expect = "true"
    #     self.assertTrue(TestCodeGen.test(input,expect,523))
    # def test_binary_andor_5(self):
    #     input = Program([VarDecl(Id('a'),IntType()),
       
    #     FuncDecl(Id('main'),[],[],
    #     [
    #     CallStmt(Id('putBool'),[BinaryOp('and',BooleanLiteral(True),BinaryOp('or', BooleanLiteral(False), BooleanLiteral(False)))])])])
    #     expect = "false"
    #     self.assertTrue(TestCodeGen.test(input,expect,524))
    # def test_relation_expression_6(self):
    #     input = Program([VarDecl(Id('a'),IntType()),
    #     VarDecl(Id('b'),IntType()),
    #     VarDecl(Id('c'),IntType()),
    #     VarDecl(Id('d'),BoolType()),
    #     FuncDecl(Id('main'),[],[],
    #     [Assign(Id('a'),IntLiteral(5)),
    #     Assign(Id('b'),IntLiteral(6)),
    #     CallStmt(Id('putBool'),[BinaryOp('<>',Id('b'),BinaryOp('*', Id('a'), IntLiteral(2)))])])])
    #     expect = "true"
    #     self.assertTrue(TestCodeGen.test(input,expect,525))

    # def test_relation_expression_9(self):
    #     input = Program([VarDecl(Id('a'),IntType()),
    #     VarDecl(Id('b'),IntType()),
    #     VarDecl(Id('c'),IntType()),
    #     VarDecl(Id('d'),BoolType()),
    #     FuncDecl(Id('main'),[],[],
    #     [Assign(Id('a'),IntLiteral(5)),
    #     Assign(Id('b'),IntLiteral(10)),
    #     CallStmt(Id('putBool'),[BinaryOp('=',BinaryOp('mod',Id('b'),IntLiteral(2)),IntLiteral(0))])])])
    #     expect = "true"
    #     self.assertTrue(TestCodeGen.test(input,expect,526))
    # def test_relation_expression_10(self):
    #     input = Program([VarDecl(Id('a'),IntType()),
    #     VarDecl(Id('b'),IntType()),
    #     VarDecl(Id('c'),IntType()),
    #     VarDecl(Id('d'),BoolType()),
    #     FuncDecl(Id('main'),[],[],
    #     [Assign(Id('a'),IntLiteral(5)),
    #     Assign(Id('b'),IntLiteral(10)),
    #     CallStmt(Id('putBool'),[BinaryOp('or',BinaryOp('>',Id('a'),Id('b')),BinaryOp('and',BinaryOp('=',BinaryOp('mod',Id('b'),IntLiteral(2)),IntLiteral(0)),BinaryOp('>',BinaryOp('*',Id('b'),IntLiteral(2)),IntLiteral(18))))])])])
    #     expect = "true"
    #     self.assertTrue(TestCodeGen.test(input,expect,527))
    # def test_unaryOp_1(self):
    #     input = Program([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),FloatType()),FuncDecl(Id('main'),[],[],
    #     [Assign(Id('a'),IntLiteral(5)),
    #     CallStmt(Id('putInt'),[UnaryOp('-',Id('a'))])])
    #     ])
    #     expect = "-5"
    #     self.assertTrue(TestCodeGen.test(input,expect,528))
    # def test_unaryOp_2(self):
    #     input = Program([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),FloatType()),FuncDecl(Id('main'),[],[],
    #     [Assign(Id('b'),FloatLiteral(5.5)),
    #     CallStmt(Id('putFloat'),[UnaryOp('-',UnaryOp('-',UnaryOp('-',Id('b'))))])])
    #     ])
    #     expect = "-5.5"
    #     self.assertTrue(TestCodeGen.test(input,expect,529))
    def test_unaryOp_3(self):
        input = Program([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),BoolType()),FuncDecl(Id('main'),[],[],
        [Assign(Id('b'),BooleanLiteral(True)),
        CallStmt(Id('putBool'),[UnaryOp('not', Id('b'))])])
        ])
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,530))
    def test_unaryOp_3(self):
        input = Program([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),BoolType()),FuncDecl(Id('main'),[],[],
        [Assign(Id('b'),BooleanLiteral(True)),
        CallStmt(Id('putBool'),[UnaryOp('not', Id('b'))])])
        ])
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,531))




















































    # def test_int(self):
    #     """Simple program: int main() {} """
    #     input = """input = Program([VarDecl(Id('a')])"""
    #     expect = "100"
    #     self.assertTrue(TestCodeGen.test(input,expect,500))
    # def test_int_ast(self):
    # 	input = Program([
    #         VarDecl(Id('a'), StringType())
    # 		])
    # 	expect = "5"
    # 	self.assertTrue(TestCodeGen.test(input,expect,501))

    # def test_int_ast(self):
    #     input = Program([
    #             FuncDecl(Id('main'),
    #                 [],
    #                 [VarDecl(Id('a'),IntType()),VarDecl(Id('b'),IntType()), VarDecl(Id('c'),IntType())],
    #                 [
    #                     Assign(Id("a"),IntLiteral(5)),
    #                     Assign(Id("b"),IntLiteral(6)),
    #                     If(BinaryOp( '>', Id('a'),Id('b')),[Assign(Id("c"),IntLiteral(1))], [Assign(Id("c"),IntLiteral(2))])
    #                 ]),
               
    #             ])
    #     expect = "5"
    #     self.assertTrue(TestCodeGen.test(input,expect,502))

    # def test_float_ast(self):
    #     input = Program([
    # 		FuncDecl(Id("main"),[],[],[
    #             #Assign(Id("b"),UnaryOp('-', IntLiteral(5))),
    # 			#Assign(Id("a"), BinaryOp('+', Id('b'), FloatLiteral(5.2142)))
    #         ]),
    #         FuncDecl(Id("abc"),[VarDecl(Id('d'), FloatType())],[VarDecl(Id('a'), FloatType()), VarDecl(Id('b'), FloatType())],[
    #             Assign(Id("d"),UnaryOp('-', IntLiteral(5))),
    # 			#Assign(Id("a"), BinaryOp('+', Id('b'), FloatLiteral(5.2142)))
    #         ])
    #     ])
    #     expect = "5.212"
    #     self.assertTrue(TestCodeGen.test(input,expect,502))
    # def test_binary_add(self):
    #     input = Program([
    # 		FuncDecl(Id("main"),[],[],[
    # 			CallStmt(Id("putFloat"),[BinaryOp("-", FloatLiteral(2.0), IntLiteral(1))])])])
    #     expect = '1.0'
    #     self.assertTrue(TestCodeGen.test(input,expect,503))
    # def test_binary_add(self):
    #     input = Program([VarDecl(Id("c"), IntType()),
    #                 FuncDecl(Id("abc"),[], [VarDecl(Id("b"), IntType())], [While(BooleanLiteral('true'),[Return(IntLiteral(1))]), Return(IntLiteral(2))], IntType()),
    #                 FuncDecl(Id("main"),[],[VarDecl(Id("a"), IntType()),VarDecl(Id("b"), IntType()), VarDecl(Id("d"), IntType())],
    #                     [
    #                         Assign(Id("a"),IntLiteral(5)),
    #                         Assign(Id("b"),IntLiteral(6)),
    #                         CallStmt(Id("abc"), []),
    #                        # While(BinaryOp(">", Id("a"), Id("b")),[Assign(Id("a"), BinaryOp( '-', Id("a"), IntLiteral(1)))])
    #                        ], 
    #                        )])
    #     expect = '1.0'
    #     self.assertTrue(TestCodeGen.test(input,expect,502))

    