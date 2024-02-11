#   COMPILADORES
#   PRACTICA 5
#   Creado por: Julio Cesar Hernandez Reyes
#   Fecha: 10 Mayo 2022
#   ENTRADAS:
#       -cadena compuesta por cualquier suma y multiplicacion de dos variables con parentesis o 0 u 1
#   SALIDA:
#       -Validacion del automata, si pertenece o no a la gramatica programada

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
#   3.-   ID -> a | b | IDa | IDb

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
#   R = X
#   α = +M
#   β = M
#   E -> E+M | M
#
# ~ E -> MX
# ~ X -> +MX | ε


#   REGLA 2
#   A = M
#   R = Y
#   α = *ID
#   β = ID
#   M -> M*ID | ID
#
# ~ M -> IDY
# ~ Y -> *IDY | ε


#   REGLA 3
#   A = ID
#   R = Z
#   α1 = a
#   β1 = a
#
#   ID -> IDa | a
#      ID -> aZ
#      Z -> aZ | ε
#
#   α2 = b
#   β2 = b
#   ID -> IDb | b
#      ID -> bZ
#      Z -> bZ | ε
#
# ~ ID -> aZ | bZ
# ~ Z -> aZ | bZ | ε
# Haciendo el cambio que ID => I
# REGLAS FINALES PARA PROGRAMAR
# ~ E -> MX
# ~ X -> +MX | ε

# ~ M -> IY
# ~ Y -> *IY | ε

# ~ I -> aZ | bZ
# ~ Z -> aZ| bZ | ε
import copy

class Pila:  # Creamos la clase Pila
    # Inicializacion del stack
    def __init__(self):
        self.items = []
    # Para poder usar print en nuestro stack
    def __str__(self):
        return str(self.items)

    #Metodo para obtener el tamaño actual de la pila
    def getSize(self):
        return self.size

    #Metodo para checar si la pila esta vacia
    def isEmpty(self):
        return self.size == 0

    #Metodo para conseguir el item que esta en el top del stack
    def top(self):
        return self.items[-1]

    # Metodo para insertar elementos a la pila
    def push(self, item):
        self.items.append(item)

    # Metodo para eliminar el ultimo elemento apilado
    def pop(self):
        return self.items.pop()




def LoopRecursiva(cadena, i, stack):
    tope = stack.top()
    print(tope, end='')
    #   Logica para validacion
    if i >= len(cadena):
        return

    #   Logica para terminales
    if stack.top() == 'a' and cadena[i] == 'a':
        stack.pop()
        LoopRecursiva(cadena, i + 1, stack)
    if stack.top() == 'b' and cadena[i] == 'b':
        stack.pop()
        LoopRecursiva(cadena, i + 1, stack)
    if stack.top() == '+' and cadena[i] == '+':
        stack.pop()
        LoopRecursiva(cadena, i + 1, stack)
    if stack.top() == '*' and cadena[i] == '*':
        stack.pop()
        LoopRecursiva(cadena, i + 1, stack)

    #   Logica para los no terminales
    # ~ E -> MX
    if stack.top() == 'E':
        stack.pop()  # saca E
        stack.push('X')
        stack.push('M')
        LoopRecursiva(cadena, i, stack)

    # ~ X -> +MX | ε
    if stack.top() == 'X':
        new_stack = copy.deepcopy(stack)
        stack.pop()  #Saca X
        stack.push('X')
        stack.push('M')
        stack.push('+')
        LoopRecursiva(cadena, i, stack)
        new_stack.pop()  #Saca X
        LoopRecursiva(cadena, i, new_stack)

    # ~ M -> IY
    if stack.top() == 'M':
        stack.pop()  # saca M
        stack.push('Y')
        stack.push('I')
        LoopRecursiva(cadena, i, stack)

    # ~ Y -> *IY | ε
    if stack.top() == 'Y':
        new_stack = copy.deepcopy(stack)
        stack.pop()  # saca Y
        stack.push('Y')
        stack.push('I')
        stack.push('*')
        LoopRecursiva(cadena, i, stack)
        new_stack.pop()  # saca Y
        LoopRecursiva(cadena, i, new_stack)

    # ~ I -> aZ | bZ
    if stack.top() == 'I':
        new_stack = copy.deepcopy(stack)
        stack.pop()  # saca I
        stack.push('Z')
        stack.push('a')
        LoopRecursiva(cadena, i, stack)
        new_stack.pop()  # saca I
        new_stack.push('Z')
        new_stack.push('b')
        LoopRecursiva(cadena, i, new_stack)

    # ~ Z -> aZ| bZ | ε
    if stack.top() == 'Z':
        new_stack2 = copy.deepcopy(stack)
        new_stack3 = copy.deepcopy(stack)

        stack.pop()  # saca Z
        stack.push('Z')
        stack.push('a')
        LoopRecursiva(cadena, i, stack)

        new_stack2.pop()  # saca Z
        new_stack2.push('Z')
        new_stack2.push('b')
        LoopRecursiva(cadena, i, new_stack2)

        new_stack3.pop()  # saca Z
        LoopRecursiva(cadena, i, new_stack3)



if __name__ == '__main__':
    print("Inicio")
    cadena = input("Favor de ingresar la cadena a validar:")
    print(cadena)

    pila = Pila()  # Crear la instancia de la pila
    pila.push('#')
    pila.push('E')
    print(pila)
    LoopRecursiva(cadena, 0, pila)
    print()
    tope = pila.top()
    if tope == '#':
        print("La cadena es valida")
    else:
        print("La cadena no es valida")

