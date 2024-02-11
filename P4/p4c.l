digit [0-9]
decimal [+-]?{digit}+"."{digit}+
entero [+-]?{digit}+
mod [Mm][Oo][Dd]"("{entero}","{entero}")"
%%
[A-Za-z_][A-Za-z0-9_]* {printf("Nombre de variable\n");}
{entero} {printf("Número entero\n");}
{decimal} {printf("Numero decimal\n");}
({decimal}|{entero})"^"({decimal}|{entero}) {printf("Potencia\n");}
({decimal}|{entero})"+"({decimal}|{entero}) {printf("Suma\n");}
({decimal}|{entero})"-"({decimal}|{entero}) {printf("Resta\n");}
({decimal}|{entero})"*"({decimal}|{entero}) {printf("Multiplicación\n");}
({decimal}|{entero})"/"({decimal}|{entero}) {printf("División\n");}
{mod} {printf("Módulo\n");}
