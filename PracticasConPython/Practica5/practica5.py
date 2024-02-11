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
#   Σ = {+,*,a,b}

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
#   α2 = b
#   β2 = b
#   ID -> IDa | a | IDb | b
#
# ~ ID -> aR3 | bR3
# ~ R3 -> aID| bID | ε


#   REGLA 1
#   A = E
#   α = +M
#   β = M
#   E -> E+M | M
#
# ~ E -> MR
# ~ R -> +MR | ε

def T_E(cadena):    
    new_cadena = cadena.replace('E','MR')    
    print(new_cadena)
    return new_cadena



def T_R(cadena):        
    new_cadena = cadena.replace('R','+MR')    
    print(new_cadena)
    return new_cadena
    


def T_R_ε(cadena):
    new_cadena = cadena.replace('R','')    
    print(new_cadena)       
    return new_cadena

#   REGLA 2
#   A = M
#   α = *ID
#   β = ID
#   M -> M*ID | ID
#
# ~ M -> IDR2
# ~ R2 -> *IDR2 | ε

def remplazar1c(cadena, old_cad, new_cad):
    i = cadena.index(old_car)
    new_cadena = cadena[:i] + new_car + cadena[i+1:]
    return new_cadena


def T_M(cadena):        
    new_cadena = remplazar1c(cadena, 'M', 'IDR2')
    print(new_cadena)       
    return new_cadena




def T_R2(cadena):
    new_cadena = cadena.replace('R2','*IDR2')    
    print(new_cadena)
    return new_cadena


def T_R2_ε(cadena):
    new_cadena = cadena.replace('R2','')    
    print(new_cadena)
    return new_cadena


if __name__ == '__main__':

    # Idea de como programar esto
    # Hacer todas las validaciones para la cadena y si alguna es igual la cadena es valida    
    cadena = 'E'
    print(cadena)
    cad_1 = T_E(cadena)
    cad_2 = T_R(cad_1)
    cad_3 = T_M(cad_2)
    cad_4 = T_M(cad_3)
    #cad_4 = T_R2(cad_3)

