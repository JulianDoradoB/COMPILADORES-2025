grammar ForLang;

prog : stat+ EOF ;

stat
  : forStat
  | assignStat
  ;

forStat
  : FOR '(' assignStat condition ';' assignStat ')' '{' stat+ '}'
  ;

assignStat
  : ID '=' expr ';'
  ;

condition
  : expr '<' expr
  ;

expr
  : expr '+' expr
  | expr '-' expr
  | expr '*' expr
  | expr '/' expr
  | INT
  | ID
  | '(' expr ')'
  ;

FOR : 'for' ;
ID  : [a-zA-Z_][a-zA-Z_0-9]* ;
INT : [0-9]+ ;
WS  : [ \t\r\n]+ -> skip ;
