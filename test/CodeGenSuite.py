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
    
    def test_assign_5(self):
        input = Program([
            VarDecl(Id('a'),IntType()),
            VarDecl(Id('b'),BoolType()),
            FuncDecl(Id('main'),[],[],[Assign(Id('b'),BooleanLiteral('TRue')),CallStmt(Id('putBool'),[Id('b')])])
            ])
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,505))

    




















































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

    