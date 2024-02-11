#   COMPILADORES
#   PRACTICA 1
#   Creado por: Julio Cesar Hernandez Reyes
#   Fecha: 27 Febrero 2022
#   ENTRADAS:
#       -AF.txt
#       -Cadena
#   SALIDA:
#       -AF Completo (Con transiciones al estado de error)
#       -Validacion(Con manejo de errores)
import numpy as np
import networkx as nx
from anytree import Node, RenderTree

def leerAF():
    archivo = open('AF.txt', 'r')
    estados = archivo.readline()        #Leer estados
    est_final = archivo.readline()      #Leer estado/s final/es
    est_inicial = archivo.readline()    #Leer estado inicial
    alfabeto = archivo.readline()       #Leer Simbolos del alfabeto
    transicion = ""
    while True:                         #Leer linea por linea todas
        temp = archivo.readline()       #las transiciones
        transicion = transicion + temp
        if not temp:
            break
    archivo.close()
    #regresar el contenido de las cadenas del AF.txt
    return estados, est_final, est_inicial, alfabeto, transicion


def separador(cadena, lista):
    estado = ""
    caracter = ""
    while True:
        for caracter in cadena:
            if caracter == ',':
                lista.append(estado)
                estado = ""
            elif caracter == '\n':
                lista.append(estado)
                estado = ""
            else:
                estado = estado + caracter
        if caracter == '\n':
            break

def auto(cadena, est_actual, est_siguiente, conta, camino):
    if conta == len(cadena):
        return
#    verificar_transiciones(est_actual, cadena[conta], arreglo, )



def automata(arr_transicion, cadena, lista_estado_inicial, lista_estados_finales):
    renglon = len(arr_transicion)
    print("Renglones = ", end="")
    print(renglon)
    est_actual = lista_estado_inicial[0]
    root = Node(est_actual)                 #Nodo raiz igual al estado inicial
    cont_car = 0    # Contador para cadena
    camino = " "
    while True:
        if cont_car == len(cadena):
            break
        conta = 0
        while True:
            if conta == renglon:
                break
            # Verificar que pasa cuando llega esta letra en el automata
            est_sig = verificar_transiciones(est_actual, cadena[cont_car], arr_transicion, conta)
            if est_sig != 0:
                if cont_car == 0:
                    nodo = Node(est_sig, parent=root)
                else:
                    nodo = Node(est_sig, parent = nodo)
            conta = conta + 1
        cont_car = cont_car + 1
    for pre, fill, node in RenderTree(root):
        print("%s%s" % (pre, node.name))
#Usar exceptions para errores

def verificar_transiciones(actual, caracter, arreglo, conta):
    siguiente = ""
    if actual == arreglo[conta, 0]:
        if caracter == arreglo[conta, 1]:
            siguiente = arreglo[conta, 2]
            return siguiente
    else:
        return 0


def arbol():
    root = Node(10)
    diez = Node(10, parent=root)
    onces = Node(11, parent=root)
    once = Node(11, parent=root)
    diezz = Node(10, parent=diez)
    doce = Node(12, parent=once)

    for pre, fill, node in RenderTree(root):
        print("%s%s" % (pre, node.name))


if __name__ == '__main__':
    print('Datos de AF2.txt')
    estados, est_final, est_inicial, alfabeto, transicion = leerAF()

    lista_estados = []
    separador(estados, lista_estados)
    print("Estados:")
    print(lista_estados)

    lista_estados_finales = []
    separador(est_final, lista_estados_finales)
    print("Estados finales:")
    print(lista_estados_finales)

    lista_estado_inicial = []
    separador(est_inicial, lista_estado_inicial)
    print("Estado inicial:")
    print(lista_estado_inicial)

    lista_alfabeto = []
    separador(alfabeto, lista_alfabeto)
    print("Simbolos del alfabeto:")
    print(lista_alfabeto)

    lista_transiciones = []
    separador(transicion, lista_transiciones)
    print("Transiciones")

    renglon = int(len(lista_transiciones) / 3)                         #candidad de simbolos / 3
    arr_transicion = np.array(lista_transiciones).reshape(renglon, 3)  #se convierte la lista de transiciones a una matriz de tamaño [renglon,3]
    print(arr_transicion)
    cadena = "ab"
    automata(arr_transicion, cadena, lista_estado_inicial, lista_estados_finales)
    print(" ")
    arbol()
    """
    camino = ""
    root = Node(lista_estado_inicial[0])
    auto(cadena, 0, lista_estado_inicial[0], camino, arr_transicion, root)
    
    for pre, fill, node in RenderTree(root):
        print("%s%s" % (pre, node.name))
    #for element in lista_estados:
    #   print(element)
    """
    """
    print(estados, end="")
    print(est_final, end="")
    print(est_inicial, end="")
    print(alfabeto)
    print(transicion, end="")
    """ 