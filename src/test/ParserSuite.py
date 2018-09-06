import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_variable_declar(self):
        """test variable declar"""
        input="""var a , b , c : integer ;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))
    def test_variable_declar_many(self):
        """test variable declar many"""
        input="""var a , b , c : integer ; e , f : real ;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))
    def test_variable_declar_array(self):
        """test variable declar many"""
        input="""var d , b : array [    1 .. 5    ] of integer ;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,203))
    def test_variable_declar_error(self):
        """test variable declar many"""
        input="""d , b : array [    1 .. 5    ] of integer ;"""
        expect = "Error on line 1 col 0: d"
        self.assertTrue(TestParser.test(input,expect,204))
    #test function declar
    def test_function_declar(self):
        """test function declar """
        input="""function foo (a , b : integer ; c : real ) : array [ 1 .. 2 ] of integer ;
            var x , y : real ; 
            begin
            
            end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,205))
    def test_function_declar_error(self):
        """test function declar """
        input="""function foo (a , b : integer  ;) : array [ 1 .. 2 ] of integer ;
            var x , y : real ; 
            begin
            
            end"""
        expect = "Error on line 1 col 32: )"
        self.assertTrue(TestParser.test(input,expect,206))
    def test_function_declar_para_empty(self):
        """test function declar """
        input="""function foo () : array [ 1 .. 2 ] of integer ;
            var x , y : real ; 
            begin
            
            end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,207))




















    # def test_simple_program(self):
    #     """Simple program: int main() {} """
    #     input = """int main() {}"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,201))

    # def test_more_complex_program(self):
    #     """More complex program"""
    #     input = """int main () {
    #         putIntLn(4);
    #     }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,202))
    
    # def test_wrong_miss_close(self):
    #     """Miss ) int main( {}"""
    #     input = """int main( {}"""
    #     expect = "Error on line 1 col 10: {"
    #     self.assertTrue(TestParser.test(input,expect,203))