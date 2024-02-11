rango [0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]
%%
"int"|"char"|"double"|"float" {printf("Tipo de dato\n");}
\".*\" {printf("Cadena válida\n");}
[A-Za-z_][A-Za-z0-9_]* {printf("Variable válida\n");}
[0-9]+ {printf("Número entero\n");}
[0-9]*"."[0-9]+ {printf("Número decimal\n");}
{rango}"."{rango}"."{rango}"."{rango} {printf("IP VÁLIDA");}
