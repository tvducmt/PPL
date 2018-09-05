grammar MP;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

// program  : many_declare EOF;
// many_declare : variable_declare | function_declare | procedure_declare;
// variable_declare : VAR IDlist COLON ;
// IDlist : ID COMMA IDlist | ID ;

//Lexer

//Type
INTTYPE: 'integer' ;

STRINGTYPE: 'string';

BOOLEANTYPE: 'boolean';

REALTYPE: 'real';

BOOLEANLIT: 'true' | 'false';

// // CHưa làm đc chuỗi string
// fragment ESCAPE: ('\\'('b'|'f'|'r'|'n'|'t'|'\''|'\"'|'\\'));

// STRINGLIT: '"' (~[\n"\\]|ESCAPE)* '"' {
//                                             String s = getText();
//                                             s = s.substring(1,s.length()-1);
//                                             setText(s);
//                                         };

fragment Nguyen: [0-9]+;

fragment Le: '.'[0-9]*;

fragment Mu: ('e'|'E')('-')?[0-9]+;

FLOATLIT: Nguyen Mu | Nguyen Le | Le Mu | Nguyen Le Mu | Le Nguyen ;

INTLIT: [0-9]+;


//Seperator
seperators: LSB | RSB | COLON | LB | RB | SEMI | COMMA | DD;

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
			| INTTYPE | STRINGTYPE | NOT | AND | OR | INTDIV | MOD ;

BREAK: 'break';
CONTINUE: 'continue';
FOR : 'for';
TO : 'to';
DOWNTO: 'downto';
DO: 'do';
IF : 'if';
THEN : 'then';
ELSE : 'else';
RETURN : 'return';
WHILE : 'while';
BEGIN : 'begin';
END : 'end';
FUNCTION :'function';
PROCEDURE : 'procedure';
VAR : 'var';
ARRAY:'array';
OF: 'of';




//comment
fragment TranditionalBlockComment:  '(*' .*? '*)';
fragment SingleLineComment : '//' ~('\r' | '\n')* ;
fragment BlockComment : '{*' .*? '*}';
COMMENTS: (SingleLineComment | TranditionalBlockComment | BlockComment)+ ->skip ;

//ID
ID: ([a-zA-Z]|'_')([a-zA-Z0-9]|'_')*;








ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;