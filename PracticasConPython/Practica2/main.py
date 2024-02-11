#   COMPILADORES
#   PRACTICA 2
#   Creado por: Julio Cesar Hernandez Reyes
#   Fecha: 29 Marzo 2022
#   ENTRADAS:
#       -AF.txt
#       -Cadena
#   SALIDA:
#       -AF Completo (Con transiciones al estado de error)
#       -Validacion(Con manejo de errores)
#   La diferencia con la practica 1 es que se reciben transiciones con epsilon
import os


# FUNCION PARA DESPLEGAR QUE ARCHIVOS.TXT ESTAN DISPONIBLES EN EL DIRECTORIO ACTUAL
def archivosexistentes():
    print("Archivos disponibles en este directorio:")
    textos = [_ for _ in os.listdir() if _.endswith(".txt")]  # Se guardan en una lista los archivos que sean .txt
    for archivo in textos:  # Se imprimen los archivos de la lista
        print(archivo)


# FUNCION QUE LEE LOS DATOS DE UN ARCHIVO .TXT Y REGRESA LOS DATOS EN LISTAS
def leerdatos(nombrearchivo):
    # Q ->Estados del automata
    # F ->Conjunto de estados finales
    # S ->Estado inicial
    # Σ ->(sigma)->Simbolos para transiciones entre estados
    # δ ->(delta)->Transiciones entre estados

    archivo = open(nombrearchivo, "r")
    Q = archivo.readline()
    F = archivo.readline()
    S = archivo.readline()
    sigma = archivo.readline()
    # Se limpian las cadenas quitando el /n al final de cada una
    Q = Q.strip()
    F = F.strip()
    S = S.strip()
    sigma = sigma.strip()
    # Se separan los valores por comas y se guardan en una lista
    LQ = Q.split(",")
    LF = F.split(",")
    LS = S.split(",")
    Lsigma = sigma.split(",")
    # Se separan los valores de las transiciones en una lista de listas
    delta = []
    for linea in archivo.readlines():
        linea = linea.strip()  # Se limpia la cadena
        Llinea = linea.split(",")  # Se separan los valores
        delta.append(Llinea)
        # print(linea)
    archivo.close()
    # Se pueden imprimir las listas
    """
    print(LQ)
    print(LF)
    print(LS)
    print(Lsigma)
    print(delta)
    """
    # Q F S Σ δ
    return LQ, LF, LS, Lsigma, delta


# FUNCION QUE COMPLETA EL AUTOMATA CON LAS TRANSICIONES AL ESTADO DE ERROR
def completarautomata(LQ, Lsigma, delta):
    # Q ->Estados del automata
    # Σ ->(sigma)->Simbolos para transiciones entre estados
    # δ ->(delta)->Transiciones entre estados
    # ##Delta = np.array(delta) # Se convierte la lista delta en un array
    CantEsta = len(LQ)  # Cantidad de Estados    3
    CantSimb = len(Lsigma)  # Cantidad de Simbolos   2
    CantTran = len(delta)  # Cantidad de Transiciones   4
    BanderaEerror = False
    for i in range(0, CantEsta):  # For que recorre los estados existentes
        estaAct = LQ[i]
        # Proceso para entender que se hace en la busqueda de transiciones faltantes
        """
        lugarEstAct = np.where(Delta == estaAct)    # Se crea un array para guardar la ubicacion de cada coincidencia del estado actual en delta
        print(estaAct) # Impresion para dar seguimiento de lo que esta pasando
        estadosEncontrados = darcoordenadas(lugarEstAct)    # Se manda llamar funcion para encontrar coordenadas de estados encontrados
        print(estadosEncontrados)
        """
        for j in range(0, CantSimb):  # For que recorre simbolos existentes
            simbAct = Lsigma[j]
            existe = False
            # ##print(simbAct)  # Impresion para dar seguimiento de lo que esta pasando
            for k in range(0, CantTran):  # For que recorre las transiciones existentes
                # checando condiciones entre estados y simbolos para verificar si existe o no la transicion
                if estaAct == delta[k][0] and simbAct == delta[k][1]:
                    ###print("la transicion existe")
                    existe = True
                    break
            if not existe:
                ###print("Crear nuevas transiciones")
                estadoError = [estaAct, simbAct, "EE"]
                delta.append(estadoError)
                BanderaEerror = True
    if BanderaEerror:
        for i in range(0, CantSimb):
            nuevalista = ["EE", Lsigma[i], "EE"]
            delta.append(nuevalista)
    return delta


# FUNCION QUE EVALUA LAS TRANSICIONES Y REGRESA EL ESTADO SIGUIENTE DEPENDIENDO EL ESTADO ACTUAL
def transicion_estados(est_actual, caracter, delta):
    est_siguiente = []
    renglon = len(delta)  # Cantidad de transiciones
    columna = len(delta[0])  # Cantidad de elementos en cada transicion, siempre son 3
    for i in range(0, renglon):
        if est_actual == delta[i][0]:
            if caracter == delta[i][1]:
                est_siguiente.append(delta[i][2])
    # print(renglon, columna)
    return est_siguiente


class cadena:
    def __init__(self, cadenaactual):
        self.cadena = cadenaactual
        self.valida = False

    def validacion(self, LQ, LF, LS, Lsigma, delta, actual, i, Old_LCA, Old_LME):
        New_LCA = Old_LCA
        New_LME = Old_LME

        if i == len(self.cadena):  # Si ya se termino la cadena
            if actual in LF:
                self.valida = True
                print("Valida")
                print("Camino: ")
                print(New_LCA)
                print("Manejo de Errores:")
                print(New_LME)
            """
            else:
                print(New_LCA)
            """
        else:  # Si no ha terminado la cadena
            caractertemp = self.cadena[i]

            if not (caractertemp in Lsigma):  # Si el caracter no forma parte del alfabeto
                New_LME.append("" + actual + "->(" + caractertemp + ")")
                self.validacion(LQ, LF, LS, Lsigma, delta, actual, i + 1, New_LCA, New_LME)
            else:  # Si el caracter si forma parte del alfabeto
                est_sig = transicion_estados(actual, caractertemp, delta)

                if len(est_sig) == 0:  # No hay transiciones con este simbolo
                    est_sig_E = transicion_estados(actual, 'E', delta)
                    #print(est_sig_E)
                    for j in range(0, len(est_sig_E)):
                        actual_E = est_sig_E[j]
                        sentencia = actual + "(E)->" + est_sig_E[j]
                        New_LCA.append(sentencia)
                        self.validacion(LQ, LF, LS, Lsigma, delta, actual_E, i, New_LCA, New_LME)
                        largo = len(New_LCA)
                        largo = largo - 1
                        New_LCA.remove(New_LCA[largo])  # Para quitar estados repetidos al encontrar varias transiciones
                else:  # Si hay transiciones con este simbolo
                    for j in range(0, len(est_sig)):
                        actual = est_sig[j]
                        sentencia = actual + "(" + caractertemp + ")->" + est_sig[j]
                        New_LCA.append(sentencia)
                        self.validacion(LQ, LF, LS, Lsigma, delta, actual, i+1, New_LCA, New_LME)
                        largo = len(New_LCA)
                        largo = largo - 1
                        New_LCA.remove(New_LCA[largo])  # Para quitar estados repetidos al encontrar varias transiciones


if __name__ == '__main__':
    # Q ->Estados del automata
    # F ->Conjunto de estados finales
    # S ->Estado inicial
    # Σ ->(sigma)->Simbolos para transiciones entre estados
    # δ ->(delta)->Transiciones entre estados
    archivosexistentes()
    print("Ingresa Nombre del Archivo:")
    # nombrearchivo = input()
    nombrearchivo = "automata.txt"
    LQ, LF, LS, Lsigma, delta = leerdatos(nombrearchivo)
    print("Datos:")
    print(LQ)
    print(LF)
    print(LS)
    print(Lsigma)
    print(delta)
    print("Automata Completo:")
    deltacompleto = delta.copy()
    print(completarautomata(LQ, Lsigma, deltacompleto))

    print("Cadena a evaluar:")
    # estacadena = input()
    estacadena = "abaa"
    print(estacadena)

    cadenaevaluar = cadena(estacadena)
    LCA = []  # Lista para caminos
    LME = []  # Lista manejo de errores
    # LCA.append(LS[0])  # Estado inicial
    cadenaevaluar.validacion(LQ, LF, LS, Lsigma, delta, LS[0], 0, LCA, LME)
    if not cadenaevaluar.valida:
        print("Cadena no valida")
