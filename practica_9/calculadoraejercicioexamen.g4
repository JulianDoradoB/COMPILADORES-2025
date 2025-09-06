grammar calculadoraejercicioexamen;

prog: stat+ ;

stat: ID '=' expr ';'        # Asignacion
    | expr ';'               # ExprStmt
    ;

expr: expr op=('*'|'/') expr # MulDiv
    | expr op=('+'|'-') expr # AddSub
    | INT                    # Int
    | FLOAT                  # Float
    | ID                     # Variable
    | '(' expr ')'           # Parens
    ;

// Tokens
ID    : [a-zA-Z_][a-zA-Z_0-9]* ;
INT   : [0-9]+ ;
FLOAT : [0-9]+ '.' [0-9]+ ;
WS    : [ \t\r\n]+ -> skip ;
