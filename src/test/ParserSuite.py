import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
     #test var declar
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
    def test_function_declar_error_para(self):
        """test function declar para """
        input="""function foo (a , b : integer  ;) : array [ 1 .. 2 ] of integer ;
            var x , y : real ; 
            begin
            
            end"""
        expect = "Error on line 1 col 32: )"
        self.assertTrue(TestParser.test(input,expect,206))
    def test_function_empty_para(self):
        """test function declar """
        input="""function foo () : array [ 1 .. 2 ] of integer ;
            var x , y : real ; 
            begin
            
            end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,207))
    def test_wrong_miss_close(self):
        """test function declar """
        input="""function foo ( : array [ 1 .. 2 ] of integer ;
            var x , y : real ; 
            begin
            
            end"""
        expect = "Error on line 1 col 15: :"
        self.assertTrue(TestParser.test(input,expect,208))
    def test_function_named_error(self):
        """test function declar """
        input="""function 1foo (): array [ 1 .. 2 ] of integer ;
            var x , y : real ; 
            begin
            
            end"""
        expect = "Error on line 1 col 9: 1"
        self.assertTrue(TestParser.test(input,expect,209))  
    def test_function_named(self):
        """test function named """
        input="""function _ADVCDfoo     (): array [ 1 .. 2 ] of integer ;
            var x , y : real ; 
            begin
            
            end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,210))  
    def test_wrong_miss_colon(self):
        """test wrong miss colon """
        input="""function foo ()  array [ 1 .. 2 ] of integer ;
            var x , y : real ; 
            begin
            
            end"""
        expect = "Error on line 1 col 17: array"
        self.assertTrue(TestParser.test(input,expect,211))
    def test_wrong_miss_body(self):
        """test wrong miss body """
        input="""function foo () : array [ 1 .. 2 ] of integer ;
            var x , y : real ;  """
           
        expect = "Error on line 2 col 32: <EOF>"
        self.assertTrue(TestParser.test(input,expect,212))
    def test_wrong_miss_return(self):
        """ test wrong miss return """
        input="""function foo ();
            var x , y : real ; 
            begin
            
            end"""
        expect = "Error on line 1 col 15: ;"
        self.assertTrue(TestParser.test(input,expect,213))
    def test_wrong_miss_semi(self):
        """test wrong miss semi """
        input="""function foo () : array [ 1 .. 2 ] of integer 
            var x , y : real ;
            begin
            
            end"""
        expect = "Error on line 2 col 12: var"
        self.assertTrue(TestParser.test(input,expect,214))
    def test_wrong_miss_semi_var(self):
        """test wrong miss semi var """
        input="""function foo () : array [ 1 .. 2 ] of integer ;
            var x , y : real 
            begin
            
            end"""
        expect = "Error on line 3 col 12: begin"
        self.assertTrue(TestParser.test(input,expect,215))

    def test_wrong_miss_close_body(self):
        """test wrong miss body end"""
        input="""function foo () : array [ 1 .. 2 ] of integer ;
            var x , y : real ; 
            begin"""
        expect = "Error on line 3 col 17: <EOF>"
        self.assertTrue(TestParser.test(input,expect,216))
    def test_case_insensitive(self):
        """test_case_insensitive"""
        input="""FuNctIon _ADVCDfoo     (): array [ 1 .. 2 ] of integer ;
            var x , y : real ; 
            begin
            
            end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,217))
    def test_wrong_type_return(self):
        """test_wrong_type_return"""
        input="""function _ADVCDfoo     (): array [ 1 .. 2 ] of array [ 1 .. 2 ] ;
            var x , y : real ; 
            begin
            
            end"""
        expect = "Error on line 1 col 47: array"
        self.assertTrue(TestParser.test(input,expect,218))
    #test procedure declar
    def test_procedure_declar(self):
        """test_procedure_declar"""
        input="""procedure abc ();
            var x , y : real ; 
            begin
            
            end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,219))
    def test_procedure_declar(self):
        """test_procedure_declar"""
        input="""procedure abc ();
            var x , y : real ; 
            begin
            
            end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,219))
    def test_case_insensitive(self):
        """test_case_insensitive"""
        input="""prOceDure _ADVCDfoo ();
            var x , y : real ; 
            begin
            
            end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,220))
    def test_wrong_redundancy_colon(self):
        """test_wrong_redundancy_colon"""
        input="""procedure abc (): array [ 1 .. 2 ] of integer ;
            var x , y : real ; 
            begin
            
            end"""
        expect = "Error on line 1 col 16: :"
        self.assertTrue(TestParser.test(input,expect,221))
    def test_wrong_miss_semi_produre(self):
        """test_wrong_redundancy_colon"""
        input="""procedure abc ()
            var x , y : real ; 
            begin
            
            end"""
        expect = "Error on line 2 col 12: var"
        self.assertTrue(TestParser.test(input,expect,222))
    def test_wrong_miss_body_produre(self):
        """test_wrong_miss_body_produre """
        input="""procedure foo ();
            var x , y : real ;  """
           
        expect = "Error on line 2 col 32: <EOF>"
        self.assertTrue(TestParser.test(input,expect,223))
    #test Assignment Statement
    def test_assignment_stmt_simple(self):
        """test_assignment_stmt"""
        input= """procedure abc ();
            var x , y : real ; 
            begin
                a:=12;
            end"""
        expect='successful'
        self.assertTrue(TestParser.test(input,expect,224))
    def test_assignment_stmt_many(self):
        """test_assignment_stmt_many"""
        input= """procedure abc ();
            begin
                a:=b:=c:=d:=12;
            end"""
        expect='successful'
        self.assertTrue(TestParser.test(input,expect,225))
    def test_assign_stmt_with_expr(self):
        """test_assign_stmt_with_expr"""
        input= """procedure abc ();
            begin
                a:=b:=c:=d:=(12+3);
            end"""
        expect='successful'
        self.assertTrue(TestParser.test(input,expect,226))
    def test_assign_stmt_with_funcall(self):
        """test_assign_stmt_with_expr"""
        input= """procedure abc ();
            begin
                a:=b:=c:=d:=foo();
            end"""
        expect='successful'
        self.assertTrue(TestParser.test(input,expect,227))
    def test_assign_stmt_with_funcall_semi(self):
        """test_assign_stmt_with_expr"""
        input= """procedure abc ();
            begin
                a:=b:=c:=d:=foo(2+3;);
            end"""
        expect='Error on line 3 col 35: ;'
        self.assertTrue(TestParser.test(input,expect,228))
    def test_assign_stmt_with_funcall_explist(self):
        """test_assign_stmt_with_funcall_explist"""
        input= """procedure abc ();
            begin
                a:=b:=c:=d:=foo(2+3, 3*3, a AND b);
            end"""
        expect='successful'
        self.assertTrue(TestParser.test(input,expect,229))
    def test_assign_stmt_with_realtype(self):
        """test_assign_stmt_with_funcall_explist"""
        input= """procedure abc ();
            begin
                some_real := 37573.5 * 37593 + 385.8 / 367.1;
            end"""
        expect='successful'
        self.assertTrue(TestParser.test(input,expect,230))
        
    #test_if_state
    def test_ifstate(self):
        """test_ifstate"""
        input= """procedure abc ();
            begin
                if color = red then
                   a:=3;
                else
                    b:=3;
            end"""
        expect='successful'
        self.assertTrue(TestParser.test(input,expect,231))
    def test_ifstate_miss_else(self):
        """test_ifstate_miss_else"""
        input= """procedure abc ();
            begin
                if color = red then
                    b:=3;
            end"""
        expect='successful'
        self.assertTrue(TestParser.test(input,expect,232))
    def test_ifstate_miss_bodyif(self):
        """test_ifstate_miss_bodyif"""
        input= """procedure abc ();
            begin
                if color = red then
            end"""
        expect='Error on line 4 col 12: end'
        self.assertTrue(TestParser.test(input,expect,233))
    def test_ifstate_miss_exp(self):
        """test_ifstate_miss_exp"""
        input= """procedure abc ();
            begin
                if  then
                    b:=3;
            end"""
        expect='Error on line 3 col 20: then'
        self.assertTrue(TestParser.test(input,expect,234))
    def test_ifstate_wrong_exp(self):
        """test_ifstate_wrong_exp"""
        input= """procedure abc ();
            begin
                if +hello then
                    b:=3;
            end"""
        expect='Error on line 3 col 19: +'
        self.assertTrue(TestParser.test(input,expect,235))
    def test_ifstate_wrong_exp_real(self):
        """test_ifstate_wrong_exp_real"""
        input= """procedure abc ();
            begin
                if 3//4 then
                    b:=3;
            end"""
        expect='Error on line 4 col 20: b'
        self.assertTrue(TestParser.test(input,expect,236))
    def test_ifstate_have_semi(self):
        """test_ifstate_have_semi"""
        input= """procedure abc ();
            begin
                if color = red then;
                    hk:=56;
            end"""
        expect='Error on line 3 col 35: ;'
        self.assertTrue(TestParser.test(input,expect,237))
    def test_ifstate_have_semi_else(self):
        """test_ifstate_have_semi_else"""
        input= """procedure abc ();
            begin
                if color = red then
                   a:=3;
                else;
                    b:=3;
            end"""
        expect='Error on line 5 col 20: ;'
        self.assertTrue(TestParser.test(input,expect,238))
    #test_for_state 
    def test_for_state_to(self):
        """test_for_state_to"""
        input= """procedure ABC ();
            begin
                for i:= 1 to 10 do g:=5;
            end"""
        expect='successful'
        self.assertTrue(TestParser.test(input,expect,239))
    def test_for_state_downto(self):
        """test_for_state_downto"""
        input= """procedure ABC ();
            begin
                for i:= 1 downto 10 do g:=5;
            end"""
        expect='successful'
        self.assertTrue(TestParser.test(input,expect,240))












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