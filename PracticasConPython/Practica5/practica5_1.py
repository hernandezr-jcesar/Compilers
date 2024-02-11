#   COMPILADORES
#   PRACTICA 5
#   Creado por: Julio Cesar Hernandez Reyes
#   Fecha: 10 Mayo 2022
#   ENTRADAS:
#       -
#       -
#   SALIDA:
#       -
#       -

# Gramatica a programar:
#   G = {N,Σ,S,P}
#   N es una coleccion finita de no terminales
#   Σ es un alfabeto (Conjunto de Terminales)
#   S es un no terminal llamado Simbolo inicial
#   P es una coleccion finita de reglas de sustitucion llamadas producciones

#   G = {N,Σ,E,P}
#   N = {E,M,P,ID}
#   Σ = {+,*,a,b,0,1}

#   1.-   E -> E+M | M
#   2.-   M -> M*ID | ID
#   3.-   ID -> a | b | IDa | IDb | ID0 | ID1

#   LIMPIEZA DE LA GRAMATICA
#
#   Formula para la limpieza
#   -----------
#   A ->Aα | β
#       |
#       V
#   A -> βR
#   R -> αR | ε
#   ------------


#   REGLA 1
#   A = E
#   α = +M
#   β = M
#   E -> E+M | M
#
# ~ E -> MR
# ~ R -> +MR | ε


#   REGLA 2
#   A = M
#   α = *ID
#   β = ID
#   M -> M*ID | ID
#
# ~ M -> IDR2
# ~ R2 -> *IDR2 | ε

#   REGLA 3
#   A = ID
#   α = a
#   β = a
#   ID -> IDa | a
#
# ~ ID -> aR3
# ~ R3 -> aR3 | ε


#  A = ID
#   α2 = b
#   β2 = b
#   ID -> IDb | b
#
# ~ ID -> bR4
# ~ R4 -> bR4 | ε


# ~ ID -> ID0 | ID1


#   REGLA 1
#   A = E
#   α = +M
#   β = M
#   E -> E+M | M
#
# ~ E -> MR
# ~ R -> +MR | ε

def T_E(cadena):
    print("regla T_E")
    i = cadena.index('E')
    cadena[i] = "M"
    cadena[i] = "E"



def T_R(R):
    print("regla T_R")


def regla1_2():
    print("regla 1_2")


def regla2():
    print("regla 1")

def regla3():
    print("regla 1")

if __name__ == '__main__':

    # Idea de como programar esto
    # Hacer todas las validaciones para la cadena y si alguna es igual la cadena es valida
    print("Hola")
    T_E("casdafadeE")
