grammar MP;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}
//Parser--------------------------------------------------

program  : declare+ EOF;
declare : variable_declare | function_declare | procedure_declare;
variable_declare : VAR varlist ;    
varlist : variable SEMI (varlist)*;
variable : idlist COLON vartype;
idlist : ID (COMMA idlist)*;
vartype : primitive_type | compound_type ;
primitive_type: INTTYPE | STRINGTYPE | BOOLEANTYPE | REALTYPE ;
compound_type: ARRAY LSB  INTLIT DD INTLIT  RSB OF primitive_type;
function_declare : FUNCTION ID LB parameterlist RB COLON vartype SEMI variable_declare? compound_state;
parameterlist : variable  parameterl | ;
parameterl : SEMI variable parameterl | ;
procedure_declare : PROCEDURE ID LB parameterlist RB SEMI variable_declare? compound_state;
compound_state : BEGIN nullable_stmt END;
nullable_stmt : (stmt)*;
stmt:   exprStmt
            | assign_state | if_state | for_state
            | while_state | break_state | continue_state
            | return_state | call_state | compound_state | with_state|default_function;

assign_state : (ID|expr5) COLON EQUAL (ID COLON EQUAL)* expr SEMI;
if_state : IF expr THEN stmt (ELSE stmt)?;
for_state : FOR ID COLON EQUAL expr (TO|DOWNTO) expr DO stmt;
while_state : WHILE expr DO stmt;
break_state : BREAK SEMI;
continue_state : CONTINUE SEMI;
return_state : RETURN expr? SEMI;
with_state : WITH  varlist DO stmt;
call_state : fullcall SEMI;

fullcall: ID LB exprList RB ;
//expr5
//index_expr: expr LSB expr RSB;
//expr6 LSB expr RSB
  //   | expr6;
//Built-in function
default_function: GETINT LB RB SEMI 
                | PUTINT LB expr RB SEMI
                | PUTINTLN LB expr RB SEMI
                | GETFLOAT LB RB SEMI
                | PUTFLOAT LB expr RB SEMI
                | PUTFLOATLN LB expr RB SEMI
                | PUTBOOL LB expr RB SEMI
                | PUTBOOLLN LB expr RB SEMI
                | PUTSTRING LB expr RB SEMI
                | PUTSTRINGLN LB expr RB SEMI
                | PUTLN LB RB SEMI; 

GETINT: 'getInt';

PUTINT: 'putInt';

PUTINTLN: 'putIntLn';

GETFLOAT: 'getFloat';

PUTFLOAT: 'putFloat';

PUTFLOATLN: 'putFloatLn';

PUTBOOL: 'putBool';

PUTBOOLLN: 'putBoolLn';

PUTSTRING:  'putString';

PUTSTRINGLN: 'putStringLn';

PUTLN: 'putLn';

//expression
exprStmt: expr SEMI;
exprList: (expr (COMMA expr)*)?;
expr: expr AND THEN expr1
    | expr OR ELSE expr1
    | expr1;

expr1: expr2 EQUAL expr2 
    | expr2 NOTEQUAL expr2
    | expr2 LESSTHAN expr2
    | expr2 LESOREQUAL expr2
    | expr2 GREATERTHAN expr2
    | expr2 GREOREQUAL expr2 
    | expr2;

expr2: expr2 ADDITION expr3 
    |  expr2 SUBORNE expr3 
    |  expr2 OR expr3 
    | expr3;

expr3: expr3 DIVISION expr4
     | expr3 MULTIPLICATION expr4
     | expr3 MOD expr4
     | expr3 AND expr4
     | expr3 INTDIV expr4
     | expr4;

expr4:  NOT expr4
     |  SUBORNE expr4
     |  expr5;
expr5: expr6 LSB expr RSB
   | expr6;
expr6: LB expr RB
     | INTLIT | FLOATLIT | STRINGLIT | BOOLEANLIT | ID | fullcall;



//Lexer----------------------------------------------

//Type

INTTYPE: ('i'|'I')('n'|'N')('t'|'T')('e'|'E')('g'|'G')('e'|'E')('r'|'R');

STRINGTYPE: ('s'|'S')('t'|'T')('i'|'I')('n'|'N')('G'|'g');

BOOLEANTYPE: ('B'|'b')('O'|'o')('O'|'o')('L'|'l')('E'|'e')('a'|'A')('n'|'N');

REALTYPE: ('r'|'R')('e'|'E')('a'|'A')('l'|'L'|);

BOOLEANLIT: TRUE | FALSE;
 



STRINGLIT: '"' ~('\b'|'\f'|'\r'|'\n'|'\t'|'\''|'"'|'\\')* '"'{
                                              self.text= self.text.strip('"');
                                             
                                         };

    
fragment Nguyen: [0-9]+;

fragment Le: '.'[0-9]*;

fragment Mu: ('e'|'E')('-')?[0-9]+;

FLOATLIT: Nguyen Mu | Nguyen Le | Le Mu | Nguyen Le Mu | Le Nguyen ;

INTLIT: [0-9]+;


//Seperator
seperators: LSB | RSB | COLON | LB | RB | SEMI | COMMA | DD ;

//ASSIGN: ':=';

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

NOT: ('n'|'N')('o'|'O')('t'|'T');

AND: ('a'|'A')('N'|'n')('D'|'d');

OR : ('o'|'O')('r'|'R');

INTDIV : ('d'|'D')('I'|'i')('V'|'v');

MOD : ('m'|'M')('O'|'o')('D'|'d');


//Keyword
keywords: 	BREAK | CONTINUE | FOR | TO | DOWNTO | DO | IF | THEN | ELSE | RETURN | WHILE | BEGIN 
			| END | FUNCTION | PROCEDURE | VAR | BOOLEANLIT | ARRAY | OF | REALTYPE | BOOLEANTYPE 
			| INTTYPE | STRINGTYPE | NOT | AND | OR | INTDIV | MOD | TRUE | FALSE;

//BREAK: 'break';
BREAK: ('b'|'B')('r'|'R')('e'|'E')('a'|'A')('k'|'K');
CONTINUE: ('c'|'C')('o'|'O')('N'|'n')('T'|'t')('i'|'I')('n'|'N')('u'|'U')('E'|'e'); 
FOR :  ('f'|'F')('O'|'o')('r'|'R');
TO : ('t'|'T')('o'|'O');
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
WITH: ('W'|'w')('i'|'I')('T'|'t')('H'|'h');


//comment
fragment TranditionalBlockComment:  '(*' .*? '*)';
fragment SingleLineComment : '//' ~('\r' | '\n')* ;
fragment BlockComment : '{' .*? '}';
COMMENTS: (SingleLineComment | TranditionalBlockComment | BlockComment)+ ->skip ;

//ID
ID: ([a-zA-Z]|'_')([a-zA-Z0-9]|'_')*;






//Error
fragment ESCAPE: '\\'('b'|'f'|'r'|'n'|'t'|'\''|'"'|'\\');
//fragment ILLEGAL: ('\\'~('b'|'f'|'r'|'n'|'t'|'"'|'\\'|'\''));
fragment ILLEGAL: ('\\'('b'|'f'|'r'|'n'|'t'|'"'|'\\'|'\''));
fragment ESCAPE_CHAR:   '\\' 't' 
           |   '\\' 'n' 
           |	'\\' 'b'
           |	'\\' 'f'
           |	'\\' 'r'
           |	'\\' '"'
           |	'\\' '\\' ;
ILLEGAL_ESCAPE: '"'(~[\n"\\]|ESCAPE)* ILLEGAL {
                                            s = IllegalEscape(self.text[1:]);
                                            raise s;
                                        };
UNCLOSE_STRING: '"'(~[\n"\\]|ESCAPE)* {
                                            x = UncloseString(self.text[1:]);
                                            raise x;
                                        };

ERROR_CHAR: .{
                s = ErrorToken(self.text);
                raise s;
             };
