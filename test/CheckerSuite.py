import unittest
from TestUtils import TestChecker
from AST import *
from StaticCheck import *
class CheckerSuite(unittest.TestCase):
    # def test_undeclared_function(self):
    #     """Simple program: int main() {} """
    #     input = """procedure main(); begin foo();end"""
    #     expect = "Undeclared Procedure: foo"
    #     self.assertTrue(TestChecker.test(input,expect,400))

    # def test_diff_numofparam_stmt(self):
    #     """More complex program"""
    #     input = """procedure main (); begin
    #         putIntLn(2);
    #     end"""
    #     expect = "Type Mismatch In Statement: CallStmt(Id(putIntLn),[])"
    #     self.assertTrue(TestChecker.test(input,expect,401))

    # def test_undeclared_function_use_ast(self):
    #     """Simple program: int main() {} """
    #     input = Program([VarDecl(Id('putStringLns'),StringType())])
    #     expect = [Symbol("x",StringType)]
    #     self.assertTrue(TestChecker.test(input,expect,402))

    # def test_diff_numofparam_expr_use_ast(self):
    #     """More complex program"""
    #     input = Program([
    #             FuncDecl(Id("main"),[],[],[
    #                 CallStmt(Id("putIntLn"),[])])])
                        
    #     expect = "Type Mismatch In Statement: CallStmt(Id(putIntLn),[])"
    #     self.assertTrue(TestChecker.test(input,expect,403))

    # def test_diff_numofparam_t(self):
    #     """More complex program"""
    #     input = Program([
    #             FuncDecl(Id("putStringLna"),[],[],[
    #                 CallStmt(Id("getInt"),[])])])
                        
    #     expect = "Type Mismatch In Statement: CallStmt(Id(getInt),[])"
    #     self.assertTrue(TestChecker.test(input,expect,404))
    # def test_diff_function(self):
    #     """More complex program"""
    #     input = Program([
    #             FuncDecl(Id("putStringLnt"),[],[],[], StringType())])
                        
    #     expect = "Type Mismatch In Statement: CallStmt(Id(getInt),[])"
    #     self.assertTrue(TestChecker.test(input,expect,405))
    # def test_diff_funcdec(self):
    #     """More complex program"""
    #     input = Program([
    #             FuncDecl(Id("ABC"),[VarDecl(Id('a'),IntType()),VarDecl(Id('a'),FloatType())],[],[], StringType())])
                        
    #     expect = "Type Mismatch In Statement: CallStmt(Id(getInt),[])"
    #     self.assertTrue(TestChecker.test(input,expect,406))
    
    # def test_diff_funcdec1(self):
    #     """More complex program"""
    #     input = Program([
    #             FuncDecl(Id("ABC"),[VarDecl(Id('b'),FloatType())],[],[Assign(Id('b'),IntLiteral(1))])])
                        
    #     expect = "Type Mismatch In Statement: CallStmt(Id(getInt),[])"
        #self.assertTrue(TestChecker.test(input,expect,407))
# FuncDecl(Id("Abc"),[VarDecl(Id('k'),IntType())],[],[]),
    # def test_diff_funcdec1(self):
    #     """More complex program"""
    #     input = Program([
               
    #             FuncDecl(Id("ABC"),[VarDecl(Id('f'),IntType())],[],[If(BinaryOp('*',IntLiteral(3),IntLiteral(3)),[Assign(Id('x'),IntLiteral(5))],[])])])
                        
    #     expect = "Type Mismatch In Statement: CallStmt(Id(getInt),[])"
    #     self.assertTrue(TestChecker.test(input,expect,408))
    def test_diff_funcdec1(self):
        """More complex program"""
        input = Program([FuncDecl(Id("main"),[],[VarDecl(Id('x'),IntType())],[For(Id('x'),IntLiteral(1),IntLiteral(10),(True),[Continue()])] )])
                        
        expect = "Type Mismatch In Statement: CallStmt(Id(getInt),[])"
        self.assertTrue(TestChecker.test(input,expect,409))

    # def test_diff_funcdec1(self):
    #     """More complex program"""
    #     input = Program([VarDecl(Id('x'),ArrayType(-3,4, IntType()))])
                        
    #     expect = "Type Mismatch In Statement: CallStmt(Id(getInt),[])"
    #     self.assertTrue(TestChecker.test(input,expect,410))
    
    # def test_diff_funcdec1(self):
    #     """More complex program"""
    #     input = Program([
    #             FuncDecl(Id("ABC"),[VarDecl(Id('a'),IntType())],[],[If(BinaryOp('>',Id('a'),IntLiteral(1)),[Assign(Id('a'),IntLiteral(1))],[If(BinaryOp('>',Id('a'),IntLiteral(1)),[Assign(Id('a'),IntLiteral(1))],[])])]) ])
                        
    #     expect = "Type Mismatch In Statement: CallStmt(Id(getInt),[])"
    #     self.assertTrue(TestChecker.test(input,expect,411))
    #def test_diff_funcdec1(self):
    #     """More complex program"""
    #     input = Program([
               
    #             FuncDecl(Id("ABC"),[VarDecl(Id('f'),IntType())],[],[Assign(Id('f'),IntLiteral(5))],[])])
                        
    #     expect = "Type Mismatch In Statement: CallStmt(Id(getInt),[])"
    #     self.assertTrue(TestChecker.test(input,expect,408))
    # def test_diff_funcdec1(self):
    #     """More complex program"""
    #     input = Program([
    #            FuncDecl(Id("main"),[VarDecl(Id('f'),IntType())],[],[Assign(Id('f'),IntLiteral(5)), Continue()])
    #            # FuncDecl(Id("mais"),[VarDecl(Id('f'),IntType()), VarDecl(Id('a'), ArrayType(-3,4, IntType()))],[],[Assign(Id('k'),ArrayCell(Id('a'),IntLiteral(1)))]),
    #             #VarDecl(Id('k'),StringType())
    #             ])
                        
    #     expect = "Type Mismatch In Statement: CallStmt(Id(getInt),[])"
    #     self.assertTrue(TestChecker.test(input,expect,408))

    