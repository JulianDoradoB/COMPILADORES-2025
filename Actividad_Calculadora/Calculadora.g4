grammar Calculadora;

prog: (stat NEWLINE?)* EOF ;

stat
    : ID '=' expr ';'?       # Asignacion
    | expr ';'?              # ExprStat
    ;

expr
    : expr '+' expr          # Suma
    | expr '-' expr          # Resta
    | expr '*' expr          # Multiplicacion
    | expr '/' expr          # Division
    | '-' expr               # Negativo
    | '(' expr ')'           # Parentesis
    | func                   # Funcion
    | NUMBER                 # Numero
    | ID                     # Variable
    ;

func
    : ID '(' expr ')'        # FuncionSimple
    ;

NUMBER  : [0-9]+ ('.' [0-9]+)? ;
ID      : [a-zA-Z_][a-zA-Z_0-9]* ;
NEWLINE : [\r\n]+ ;
WS      : [ \t]+ -> skip ;
