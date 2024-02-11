%{
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void yyerror(char *s);

%}



%union {
	int entero;
	float decimal;
}

%token <entero> ENT
%token <decimal> DEC
%token SUM RES MUL DIV MOD
/*%token MOD*/
%token APAR CPAR
%token EOL
%token COMA

%type <entero> expent
%type <decimal> expdec

%left SUM RES
%left MUL DIV MOD
/*%left '+' '-'
%left '*' '/' MOD*/
%left APAR CPAR

/*Gramática*/
%%

input:	/*vac*/
	|input line	
/*	|input expent EOL	{printf("\tResultado= %d\n", $2);}
	|input expdec EOL	{printf("\tResultado= %.4f\n", $2);}*/
;
line:	EOL	{printf("Introduce algo, compadre\n");}
	|expent EOL	{printf("\tResultado= %d\n", $1);}
	|expdec EOL	{printf("\tResultado= %.3f\n", $1);}
;
expent: ENT {$$=$1;}
	| expent SUM expent {$$=$1+$3;}
	| expent RES expent {$$=$1-$3;}
	| RES ENT {$$=$2*(-1);}
	| SUM ENT {$$=$2;}
	| expent MUL expent {$$=$1*$3;}
/*	| expent DIV expent {if($3==0){yyerror("No puedes dividir entre cero"); exit(1);} else{$$=$1/$3;}}*/
	| APAR expent CPAR {$$=$2;}
	| MOD APAR expent COMA expent CPAR {$$=$3%$5;}
	| MOD APAR expdec COMA expdec CPAR {$$=(int)$3%(int)$5;}
	| MOD APAR expent COMA expdec CPAR {$$=$3%(int)$5;}
	| MOD APAR expdec COMA expent CPAR {$$=(int)$3%$5;}
;

expdec: DEC {$$=$1;}
	| expdec SUM expdec {$$=$1+$3;}
	| expent SUM expdec {$$=$1+$3;}
	| expdec SUM expent {$$=$1+$3;}
	| expdec RES expdec {$$=$1-$3;}
	| expent RES expdec {$$=$1-$3;}
	| expdec RES expent {$$=$1-$3;}
	| RES DEC {$$=$2*(-1);}
	| SUM DEC {$$=$2;}
	| expdec MUL expdec {$$=$1*$3;}
	| expdec MUL expent {$$=$1*$3;}
	| expent MUL expdec {$$=$1*$3;}
	| expent DIV expent {if($3==0){yyerror("No puedes dividir entre cero"); exit(1);} else{$$=$1/(float)$3;}}
	| expdec DIV expdec {if($3==0){yyerror("No puedes dividir entre cero"); exit(1);} else{$$=$1/$3;}}
	| expent DIV expdec {if($3==0){yyerror("No puedes dividir entre cero"); exit(1);} else{$$=$1/$3;}}
	| expdec DIV expent {if($3==0){yyerror("No puedes dividir entre cero"); exit(1);} else{$$=$1/$3;}}
	| APAR expdec CPAR {$$=$2;}
/*	| MOD APAR expdec COMA expdec CPAR {$$=(int)$3%(int)$5;}
	| MOD APAR expent COMA expdec CPAR {$$=(int)$3%(int)$5;}
	| MOD APAR expdec COMA expdec CPAR {$$=(int)$3%(int)$5;}*/
;

%%

main(int argc, char **argv){
	printf("OKok\n");
	yyparse();
}

void yyerror(char *s){
	fprintf(stderr,"ERROR: %s\n",s);
}
