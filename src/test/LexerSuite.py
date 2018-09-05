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
    # # def test_integer(self):
    # #    """test integers"""
    # #    self.assertTrue(TestLexer.test("123a123","123,a,123,<EOF>",104))

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
    
    # #Keywords
    # def test_keyword(self):
    #     """test keywords"""
    #     # self.assertTrue(TestLexer.test("""
    #     # break else return
    #     #     ""","""break,else,return,<EOF>""",113))
    #     self.assertTrue(TestLexer.test("""break else return false abdf""","""break,else,return,false,abdf,<EOF>""", 114))
   # Test Operator
    def test_operator(self):
        """test operator"""
       # self.assertTrue(TestLexer.test("""a=b+c*d/10""","""a,=,b,+,c,*,d,/,10,<EOF>""", 115))
        self.assertTrue(TestLexer.test("""not hey  or    mod""","""not,hey,or,mod,<EOF>""", 116))
    # #Seperator
    # def test_seperator(self):
    #     """test seperator"""
    #     self.assertTrue(TestLexer.test("""integer a[5];
    # There are many, people""","""integer,a,[,5,],;,There,are,many,,,people,<EOF>""", 117))
