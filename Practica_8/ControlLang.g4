grammar ControlLang;

prog : stat+ EOF ;

stat
    : assignStat                # AssignStatAlt
    | forStat                   # ForStatAlt
    | switchStat                # SwitchStatAlt
    | ifStat                    # IfStatAlt
    ;

assignStat
    : ID '=' expr ';'
    ;

forStat
    : 'for' '(' assignStat expr ';' assignStat ')' block
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

ifStat
    : 'if' '(' expr ')' block
    ;

block
    : '{' stat+ '}'
    ;

expr
    : expr op=('*'|'/') expr     # MulDivExpr
    | expr op=('+'|'-') expr     # AddSubExpr
    | expr op=('<' | '>' | '<=' | '>=' | '==' | '!=') expr # RelExpr
    | INT                       # IntExpr
    | ID                        # IdExpr
    | '(' expr ')'              # ParenExpr
    ;

ID  : [a-zA-Z_][a-zA-Z_0-9]* ;
INT : [0-9]+ ;

WS  : [ \t\r\n]+ -> skip ;
