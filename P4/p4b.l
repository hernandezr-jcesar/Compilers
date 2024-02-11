digit [0-9]
decimal [+-]?{digit}+"."{digit}+
entero [+-]?{digit}+
bmathop ({decimal}|{entero})("*"|"/"|"+"|"-")({decimal}|{entero})
mod [Mm][Oo][Dd]"("{entero}","{entero}")"
%%
[A-Za-z_][A-Za-z0-9_]* {printf("Nombre de variable\n");}
{entero} {printf("Número entero\n");}
{decimal} {printf("Numero decimal\n");}
({decimal}|{entero})"^"({decimal}|{entero}) {printf("Potencia\n");}
{bmathop}|{mod} {printf("Operación matemática\n");}
