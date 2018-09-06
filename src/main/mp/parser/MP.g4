grammar MP;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}
//Parser--------------------------------------------------

program  : (many_declare)+ EOF;
many_declare : variable_declare | function_declare | procedure_declare;
variable_declare : VAR varlist ;
varlist : variable SEMI (varlist)*;
variable : idlist COLON vartype;
idlist : ID (COMMA idlist)*;
vartype : primitive_type | compound_type ;
primitive_type: INTTYPE | STRINGTYPE | BOOLEANTYPE | REALTYPE ;
compound_type: ARRAY LSB  INTLIT DD INTLIT  RSB OF primitive_type;
function_declare : FUNCTION ID LB parameterlist RB COLON vartype SEMI variable_declare compound_statement;
parameterlist : variable  parameterl | ;
parameterl : SEMI variable parameterl | ;
compound_statement : BEGIN .*? END;//nullable_statement END;
//nullable_statement : (statement)*;
// statement:   assignment_state | if_state   | for_state | while_state | break_state | continue_state
//             | return_state | call_state | compound_state | with_function;
// assignment_state : (ID ASSIGN (ID)*)+ expression;

procedure_declare : PROCEDURE ID LB parameterlist RB SEMI variable_declare compound_statement;

//Lexer----------------------------------------------

//Type

INTTYPE: 'integer' ;

STRINGTYPE: 'string';

BOOLEANTYPE: 'boolean';

REALTYPE: 'real';

BOOLEANLIT: TRUE | FALSE;
 

fragment ESCAPE: '\\'('b'|'f'|'r'|'n'|'t'|'\''|'"'|'\\');

STRINGLIT: '"' (~[\b\f\r\n\t"\\]|ESCAPE)* '"'; 
                                        // {
                                        //     s = getText();
                                        //     s = s.substring(1,s.length()-1);
                                        //     setText(s);
                                        // };

// STRINGLI: '"' (ESCAPE_CHAR | ~('"'|'\\'|[\r\n]))* '"';

// fragment ESCAPE_CHAR:   '\\' 't' 
//            |   '\\' 'n' 
//            |	'\\' 'b'
//            |	'\\' 'f'
//            |	'\\' 'r'
//            |	'\\' '"'
//            |	'\\' '\\' 
//     ;
    
fragment Nguyen: [0-9]+;

fragment Le: '.'[0-9]*;

fragment Mu: ('e'|'E')('-')?[0-9]+;

FLOATLIT: Nguyen Mu | Nguyen Le | Le Mu | Nguyen Le Mu | Le Nguyen ;

INTLIT: [0-9]+;


//Seperator
seperators: LSB | RSB | COLON | LB | RB | SEMI | COMMA | DD | ASSIGN;

ASSIGN: ':=';

COLON: ':';

LB: '(' ;

RB: ')' ;

SEMI: ';' ;

LSB: '[';

RSB: ']';

COMMA: ',';

DD : '..';

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

//operator
operators : ADDITION | MULTIPLICATION | NOT | OR
         | NOTEQUAL | LESSTHAN | LESOREQUAL | INTDIV | SUBORNE 
         | DIVISION | MOD | AND | EQUAL | GREATERTHAN 
         | GREOREQUAL;

ADDITION: '+';

MULTIPLICATION: '*';

NOTEQUAL: '<>';

LESSTHAN: '<';

LESOREQUAL: '<=';

SUBORNE: '-';

DIVISION: '/';

EQUAL: '=';

GREATERTHAN: '>';

GREOREQUAL: '>=';

NOT: 'not';

AND: 'and'; 

OR : 'or';

INTDIV : 'div';

MOD : 'mod';


//Keyword
keywords: 	BREAK | CONTINUE | FOR | TO | DOWNTO | DO | IF | THEN | ELSE | RETURN | WHILE | BEGIN 
			| END | FUNCTION | PROCEDURE | VAR | BOOLEANLIT | ARRAY | OF | REALTYPE | BOOLEANTYPE 
			| INTTYPE | STRINGTYPE | NOT | AND | OR | INTDIV | MOD | TRUE | FALSE;

//BREAK: 'break';
BREAK: ('b'|'B')('r'|'R')('e'|'E')('a'|'A')('k'|'K');
CONTINUE: ('c'|'C')('o'|'O')('N'|'n')('T'|'t')('i'|'I')('n'|'N')('u'|'U')('E'|'e'); 
FOR :  ('f'|'F')('O'|'o')('r'|'R');
TO : ('t|T')('o'|'O');
DOWNTO: ('d'|'D')('o'|'O')('w'|'W')('n'|'N')('T'|'t')('o'|'O');
DO: ('D'|'d')('o'|'O');
IF :  ('i'|'I')('f'|'F');
THEN : ('t'|'T')('h'|'H')('e'|'E')('n'|'N');
ELSE : ('e'|'E')('l'|'L')('s'|'S')('e'|'E');
RETURN : ('R'|'r')('e'|'E')('t'|'T')('u'|'U')('r'|'R')('n'|'N');
WHILE :  ('W'|'w')('h'|'H')('I'|'i')('l'|'L')('E'|'e');
BEGIN : ('b'|'B')('E'|'e')('G'|'g')('I'|'i')('N'|'n');
END : ('e'|'E')('N'|'n')('D'|'d');
FUNCTION : ('f'|'F')('U'|'u')('N'|'n')('C'|'c')('t'|'T')('I'|'i')('O'|'o')('N'|'n');
PROCEDURE : ('p'|'P')('r'|'R')('o'|'O')('c'|'C')('e'|'E')('d'|'D')('u'|'U')('r'|'R')('e'|'E');
VAR : ('v'|'V')('a'|'A')('R'|'r');
ARRAY: ('a'|'A')('r'|'R')('r'|'R')('a'|'A')('y'|'Y');
OF:  ('o'|'O')('f'|'F');
TRUE : ('t'|'T')('r'|'R')('U'|'u')('E'|'e');
FALSE: ('f'|'F')('a'|'A')('l'|'L')('s'|'S')('E'|'e');



//comment
fragment TranditionalBlockComment:  '(*' .*? '*)';
fragment SingleLineComment : '//' ~('\r' | '\n')* ;
fragment BlockComment : '{*' .*? '*}';
COMMENTS: (SingleLineComment | TranditionalBlockComment | BlockComment)+ ->skip ;

//ID
ID: ([a-zA-Z]|'_')([a-zA-Z0-9]|'_')*;






//Error
fragment ILLEGAL: ('\\'~('b'|'f'|'r'|'n'|'t'|'"'|'\\'|'\''));

ILLEGAL_ESCAPE: '"' (~[\n"\\]|ESCAPE)* ILLEGAL {
                                            String s = getText();
                                            s = s.substring(1,s.length());
                                            setText(s);
                                        };
UNCLOSE_STRING: '"'(~[\n"\\]|ESCAPE)*  {
                                            String s = getText();
                                            s = s.substring(1,s.length());
                                            setText(s);
                                        };

ERROR_CHAR: .;
