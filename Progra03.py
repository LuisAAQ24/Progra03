import os
import random
import sys
import time


# Esta función crea el mapa y da inicio al juego
def iniciar_juego(tamaño, ciclo,matriz):
    """
    E: El tamaño de la matriz y un ciclo inicial (0)
    S: La matriz cuadrada con los cuadros establecidos
    R: Una matriz cuadrada 
    """
    if ciclo >= tamaño:
        os.system("cls")
        return crear_juego(matriz, tamaño,1)
    else:
        # Crear una fila de la matriz usando un bucle
        fila = []
        for _ in range(tamaño):
            fila.append(0)  # Agregar un elemento a la fila
        # Llamar recursivamente para construir la matriz
        matriz.append(fila)
        iniciar_juego(tamaño, ciclo + 1,matriz)



# Esta función gestiona el juego, mostrando las opciones del jugador y del oponente
def crear_juego(mapa,tamaño,quien):
    """
    E: Imprime el mapa
    S: Impresión del tablero y estado del juego
    R: Ninguna
    """
    time.sleep(1)
    for i in range(tamaño):
        for j in range(tamaño):
            if mapa[i][j] == 1:
                mapa[i][j] = 4
            elif mapa[i][j] == 4:
                mapa[i][j] = 5
            elif mapa[i][j] == 5:
                mapa[i][j] = 2

    for fila in mapa:
        for elemento in fila:
            if elemento == 0:
                print("[    ]", end=" ")
            if elemento == 1:
                print("[ I0 ]", end=" ")
            if elemento == 2:
                print("[ P  ]", end=" ")
            if elemento == 3:
                print("[ C  ]", end=" ")
            if elemento == 4:
                print("[ I1 ]", end=" ")  
            if elemento == 5:
                print("[ I2 ]", end=" ")
            if elemento == 6:
                print("[ U  ]", end=" ")       
        print()  # Imprime una nueva línea al final de cada fila
    print()  # Línea en blanco para mayor claridad
    verificar_victoria(mapa)
    if quien == 1:
        opcion = input("Ingrese la casilla a modificar en el formato fila, columna: ")
        fila, columna = map(int, opcion.split(","))
            
        # Verificar si la posición está dentro de los límites de la matriz
        if 0 <= fila < tamaño and 0 <= columna < tamaño:
            print("1. Iniciativa ")
            print("2. Proyecto")
            print("3. Cultura")
            opcion2 = input("¿Qué busca crear?: ")
            if opcion2 == "1":
                mapa[fila][columna] = 1
                os.system("cls")
                crear_juego(mapa, tamaño,0)
            if opcion2 == "2":
                mapa[fila][columna] = 2
                os.system("cls")
                crear_juego(mapa, tamaño,0)
            if opcion2 == "3":
                crear_cultura(mapa,fila,columna,tamaño)
            else:
                print("Seleccione una opción válida")
                os.system("cls")
                crear_juego(mapa, tamaño,1)
        else:
            print("La posición está fuera de los límites de la matriz.")
            os.system("cls")
            crear_juego(mapa, tamaño,1)
    else:
        tirarOponente(mapa, tamaño//2)

def crear_cultura(mapa,fila,columna,tamaño):
    print("1. Expansión vertical")
    print("2. Expansión horizontal")
    opcion = input("Escoja una dirección: ")
    if opcion == "1":  # Expansión vertical
        for i in range(len(mapa)):
            if mapa[i][columna] in [6,0]:
                mapa[i][columna] = 3

        os.system("cls")
        crear_juego(mapa, tamaño,0)

    elif opcion == "2":  # Expansión horizontal
        for j in range(len(mapa)):
            if mapa[fila][j] in [6,0]:
                mapa[fila][j] = 3
        os.system("cls")
        crear_juego(mapa, tamaño,0)
    
    else:
        print("Opción no válida")
        os.system("cls")
        crear_juego(mapa, tamaño,1)



# Función para gestionar el turno del oponente
def tirarOponente(mapa, tiradas):
    """
    E: Mapa, resultado del dado, estado de las piezas
    S: Actualización del tablero tras el turno del oponente
    R: Ninguna
    """
    time.sleep(1)
    tamaño = tiradas*2

    for _ in range(tiradas):
        fila = random.randint(0, tamaño - 1)  # Genera un número aleatorio para la fila
        columna = random.randint(0, tamaño - 1)  # Genera un número aleatorio para la columna
        
        # Cambiar el valor en la posición seleccionada
        if mapa[fila][columna] in [0, 2, 3]:
            mapa[fila][columna] = 6
            tiradas -=1
            print(f"El oponente usurpa la casilla ({fila}, {columna})")
            time.sleep(1)
    os.system("cls")
    crear_juego(mapa, tamaño,1)
    

def verificar_victoria(matriz):
    """
    Verifica si al menos una fila o columna de la matriz está compuesta por el mismo valor (1 o 2).

    E: matriz (lista de listas)
    S: True si al menos una fila o columna tiene todos sus elementos iguales a 1 o 2, False en caso contrario
    """
    tamaño = len(matriz)

    # Verificar filas
    for fila in range(tamaño):
        if all(elemento == 2 for elemento in matriz[fila]):
            print("Victoria para los indígenas")
            time.sleep(2)
            os.system("cls")
            mostrarMenu()
        elif all(elemento == 6 for elemento in matriz[fila]):
            print("Victoria para los usurpadores")
            time.sleep(2)
            os.system("cls")
            mostrarMenu()


    # Verificar columnas
    for columna in range(tamaño):
        if all(matriz[fila][columna] == 2 for fila in range(tamaño)):
            print("Victoria para los indígenas")
            time.sleep(2)
            os.system("cls")
            mostrarMenu()
        elif all(matriz[fila][columna] == 6 for fila in range(tamaño)):
            print("Victoria para los usurpadores")
            time.sleep(2)
            os.system("cls")
            mostrarMenu()


# Conversión de string a número entero
def intNumero(str):
    """
    E: Un string numérico
    S: El valor numérico correspondiente
    R: Ninguna
    """
    diccionarioNum = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "0": 0,
                       "10": 10, "11": 11, "12": 12, "13": 13, "14": 14, "15": 15, "16": 16, "17": 17, "18": 18, "19": 19, "20": 20}
    return diccionarioNum[str]


#Conversión de un int a str
def strNumero(str):
    """
    E: Un str
    S: El str en forma de int
    R: Que sea un str
    """
    diccionarioNum = {1: "1", 2: "2", 3: "3", 4: "4",
                      5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 0: "0"}
    return diccionarioNum[str]








#Función que muestra el menú principal
def mostrarMenu():
    """
    E: Ninguna
    S: Da inicio al juego o lo finaliza
    R: Ninguna
    """
    print("-------------")
    print("Bienvenido/a al juego")
    print("-------------")
    print("")
    print("1. Iniciar a Jugar")
    print("2. Instrucciones")
    print("3. Salir")
    print("-------------")
    opcion = input("Ingrese su opción: ")
    if opcion == "1":
        tamaño = input("Ingrese el tamaño del mapa: ")
        if 2 <= intNumero(tamaño) <= 12:
            iniciar_juego(intNumero(tamaño), 0,[])
        else:
            print("Seleccione un tamaño entre 2 y 12")
            os.system("cls")
            mostrarMenu()
            
    elif opcion == "3":
        os.system("cls")
        sys.exit(0)
    else:
        print("Opción inválida. Por favor, inténtelo de nuevo.")
        time.sleep(1)
        os.system("cls")
        mostrarMenu()


mostrarMenu()
