%{
#include <stdlib.h>
#include <stdio.h>
#include "p6b.tab.h"
%}

%option noyywrap

entero [0-9]+
decimal [0-9]*"."[0-9]+
mod [Mm][Oo][Dd]

%%
[ \t]	{/*ignorar*/}
{entero} {yylval.entero=atoi(yytext); return ENT;}
{decimal} {yylval.decimal=atof(yytext); return DEC;}
"+" {return SUM;}
"-" {return RES;}
"*" {return MUL;}
"/" {return DIV;}
{mod} {return MOD;}
"(" {return APAR;}
"," {return COMA;}
")" {return CPAR;}
\n {return EOL;}
. {printf("NOPNEL %c\n", *yytext);}
%%
