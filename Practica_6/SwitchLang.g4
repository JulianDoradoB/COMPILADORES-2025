grammar SwitchLang;

prog : stat+ EOF ;

stat
    : assignStat        # AssignStatAlt
    | switchStat        # SwitchStatAlt
    ;

assignStat
    : ID '=' expr ';'
    ;

switchStat
    : 'switch' '(' ID ')' '{' caseStat+ defaultStat? '}'
    ;

caseStat
    : 'case' INT ':' stat+
    ;

defaultStat
    : 'default' ':' stat+
    ;

expr
    : INT                  # IntExpr
    | ID                   # IdExpr
    | expr '+' expr        # AddExpr
    | expr '-' expr        # SubExpr
    | expr '*' expr        # MulExpr
    | expr '/' expr        # DivExpr
    | '(' expr ')'         # ParenExpr
    ;

ID  : [a-zA-Z_][a-zA-Z_0-9]* ;
INT : [0-9]+ ;

WS  : [ \t\r\n]+ -> skip ;
