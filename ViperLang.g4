grammar ViperLang;

// Root of the program
prog: stat+ EOF ;

// Advanced Statements
stat: 'print' '(' expr ')' ';'                  # printStat
    | ID '=' expr ';'                           # assignStat
    | 'if' '(' expr ')' '{' stat* '}'           # ifStat
    | 'while' '(' expr ')' '{' stat* '}'        # whileStat
    ;

// Expressions
expr: expr op=('*'|'/') expr                    # mulDivExpr
    | expr op=('+'|'-') expr                    # addSubExpr
    | expr op=('>'|'<'|'==') expr               # compareExpr
    | INT                                       # intExpr
    | ID                                        # idExpr
    ;

// Tokens
ID  : [a-zA-Z_][a-zA-Z0-9_]* ;
INT : [0-9]+ ;
WS  : [ \t\r\n]+ -> skip ;