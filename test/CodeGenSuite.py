import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
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
    def test_binary_add(self):
        input = Program([VarDecl(Id("c"), IntType()),
                    FuncDecl(Id("abc"),[], [VarDecl(Id("b"), IntType())], [While(BooleanLiteral('true'),[Assign(Id("b"),IntLiteral(6)),Return(IntLiteral(1))])], IntType()),
                    FuncDecl(Id("main"),[],[VarDecl(Id("a"), IntType()),VarDecl(Id("b"), IntType()), VarDecl(Id("d"), IntType())],
                        [
                            Assign(Id("a"),IntLiteral(5)),
                            Assign(Id("b"),IntLiteral(6)),
                            CallStmt(Id("abc"), []),
                           # While(BinaryOp(">", Id("a"), Id("b")),[Assign(Id("a"), BinaryOp( '-', Id("a"), IntLiteral(1)))])
                           ], 
                           )])
        expect = '1.0'
        self.assertTrue(TestCodeGen.test(input,expect,502))

    