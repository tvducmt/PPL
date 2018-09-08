import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    # #ID 
    # def test_identifier(self):
    #    """test identifiers"""
    #    self.assertTrue(TestLexer.test("abc","abc,<EOF>",101))
    #    self.assertTrue(TestLexer.test("aCBbdc","aCBbdc,<EOF>",102))
    #    self.assertTrue(TestLexer.test("aAsVN","aAsVN,<EOF>",103))
    #    self.assertTrue(TestLexer.test("_Abc1","_Abc1,<EOF>",104))
    #    self.assertTrue(TestLexer.test("_123 a_123 1_2adv","_123,a_123,1,_2adv,<EOF>",105))
    #    self.assertTrue(TestLexer.test("1abc","1,abc,<EOF>",106))
    
    # #Comment
    # def test_comment(self):
    #     """test comment"""
    #     self.assertTrue(TestLexer.test("""//Comment the single comment
    #           } int main { ""","""},int,main,{,<EOF>""", 107))
    #     self.assertTrue(TestLexer.test("(**) input","input,<EOF>", 108))
    #     self.assertTrue(TestLexer.test("{**} input","input,<EOF>", 109))
    #     self.assertTrue(TestLexer.test("""//sdgdfg (*hello*)
    #         comment the single line""", """comment,the,single,line,<EOF>""", 110))
    #     self.assertTrue(TestLexer.test("{*comment // comment line*} input","input,<EOF>", 111))
    #     self.assertTrue(TestLexer.test("""(*
    #                                 * Duc
    #                                 * Tran
    #                                 * 
    #                                 *
    #                                 *
    #                                 *
    #                                 *) } int main {""","""},int,main,{,<EOF>""", 112))
    
    #Keywords
    # def test_keyword(self):
    #     """test keywords"""
        # self.assertTrue(TestLexer.test("""
        # breaK Else return
        #     ""","""breaK,Else,return,<EOF>""",113))
        # self.assertTrue(TestLexer.test("""break else return false abdf""","""break,else,return,false,abdf,<EOF>""", 114))
        # self.assertTrue(TestLexer.test("""
        # BreaK break return
        #     ""","""BreaK,break,return,<EOF>""",115))
        # self.assertTrue(TestLexer.test("""
        # continue for to downto CoNtinuE
        #     ""","""continue,for,to,downto,CoNtinuE,<EOF>""",116))
        
        
   # Test Operator
    # def test_operator(self):
    #     """test operator"""
    #     self.assertTrue(TestLexer.test("""a=b+c*d/10""","""a,=,b,+,c,*,d,/,10,<EOF>""", 117))
    #     self.assertTrue(TestLexer.test("""not hey  or    mod""","""not,hey,or,mod,<EOF>""", 118))
    # #Seperator
    # def test_seperator(self):
    #     """test seperator"""
    #     self.assertTrue(TestLexer.test("""integer a[5];
    # There are many, people ..""","""integer,a,[,5,],;,There,are,many,,,people,..,<EOF>""", 119))
    # # INTLIT
    # def test_intlit(self):
    #     """test intlit"""
    #     self.assertTrue(TestLexer.test("a=1000", "a,=,100,<EOF>", 120))
    # FLOATLIT
    #def test_floatlit(self):
    #    """test FLOATLIT"""
        # self.assertTrue(TestLexer.test("1.2", "1.2,<EOF>", 121))
        # self.assertTrue(TestLexer.test("1.", "1.,<EOF>", 122))
        # self.assertTrue(TestLexer.test(".1", ".1,<EOF>", 123))
        # self.assertTrue(TestLexer.test("1e2", "1e2,<EOF>", 124))
        # self.assertTrue(TestLexer.test("1.2E-2", "1.2E-2,<EOF>", 125))
        # self.assertTrue(TestLexer.test("9.0", "9.0,<EOF>", 126))
        # self.assertTrue(TestLexer.test("12e8", "12e8,<EOF>", 127))
        # self.assertTrue(TestLexer.test("0.33E-3", "0.33E-3,<EOF>", 128))
        # self.assertTrue(TestLexer.test("128e-42", "128e-42,<EOF>", 129))
        # self.assertTrue(TestLexer.test("e-12", "e,-,12,<EOF>", 130))
        # self.assertTrue(TestLexer.test("143e", "143,e,<EOF>", 131))
        #self.assertTrue(TestLexer.test("""1.2e-2 .1E2 9.0 12e8 0.33E-3 128e-42""", """1.2e-2,.1E2,9.0,12e8,0.33E-3,128e-42,<EOF>""", 132))
        #self.assertTrue(TestLexer.test("e-12", "e,-,12,<EOF>", 133)) 
        #self.assertTrue(TestLexer.test("23e", "23,e,<EOF>", 133))
    #boolean literal
    def test_booleanlit(self):
        self.assertTrue(TestLexer.test("true false hello", "true,false,hello,<EOF>", 132))
        #self.assertTrue(TestLexer.test("True False hello", "True,False,hello,<EOF>", 133))
    # def test_stringlit(self):
    #     self.assertTrue(TestLexer.test(""" "hello" """, """hello,<EOF>""", 134))
    
    # def test_integer(self):
    #    """test integers"""
    #    self.assertTrue(TestLexer.test("123a123","123,a123,<EOF>",135))
    #    self.assertTrue(TestLexer.test("a = 1000;","a,=,1000,;,<EOF>",136))
    #    self.assertTrue(TestLexer.test(" -5000","-,5000,<EOF>",137))
    #    self.assertTrue(TestLexer.test(" - 8000","-,8000,<EOF>",138))
    #    self.assertTrue(TestLexer.test(" --8000","-,-,8000,<EOF>",139))

    def test_stringlit(self):
        """test stringlit"""
        #self.assertTrue(TestLexer.test(' "hello" ','"hello",<EOF>',140))
        self.assertTrue(TestLexer.test('"hell okkk asd"',"""Unclosed String: hell	 okkk asd""",140))
        #self.assertTrue(TestLexer.test(' "hello i am duc" ','"hello i am duc",<EOF>',140))
        #self.assertTrue(TestLexer.test(""""abc""",'Unclosed String: "abc',141))
        #self.assertTrue(TestLexer.test(""""edf
         #                                abc" ""","""Illegal Escape In String: "edf""",142))
      #  self.assertTrue(TestLexer.test(""" "string  
       # 123" """,'Illegal Escape In String: "string',143))
        #self.assertTrue(TestLexer.test('"string\t123','Unclosed String: "string	123',144))
    #    self.assertTrue(TestLexer.test(" - 8000","-,8000,<EOF>",138))
    #    self.assertTrue(TestLexer.test(" --8000","-,-,8000,<EOF>",139))
