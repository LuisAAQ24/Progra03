# PROYECTO 3 DE TALLER DE PROGRAMACION
# SEMESTRE II 2024

import os
import random

def iniciar_juego(tamaño, ciclo, matriz):
    """
    E: El tamaño de la matriz y un ciclo inicial (0)
    S: La matriz cuadrada con los cuadros establecidos
    R: Una matriz cuadrada 
    """
    if ciclo >= tamaño:
        os.system("cls")
        return crear_juego(matriz, tamaño, 1)
    else:
        # Crear una fila de la matriz usando un bucle
        fila = [0] * tamaño  # Inicializa una fila con ceros
        matriz += [fila]  # Agrega la fila a la matriz
        iniciar_juego(tamaño, ciclo + 1, matriz)

# Esta función gestiona el juego, mostrando las opciones del jugador y del oponente
def crear_juego(mapa, tamaño, quien):
    """
    E: Imprime el mapa
    S: Impresión del tablero y estado del juego
    R: Ninguna
    """
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
            elif elemento == 1:
                print("[ I0 ]", end=" ")
            elif elemento == 2:
                print("[ P  ]", end=" ")
            elif elemento == 3:
                print("[ C  ]", end=" ")
            elif elemento == 4:
                print("[ I1 ]", end=" ")  
            elif elemento == 5:
                print("[ I2 ]", end=" ")
            elif elemento == 6:
                print("[ U  ]", end=" ")       
        print()  # Imprime una nueva línea al final de cada fila
    print()  # Línea en blanco para mayor claridad
    verificar_victoria(mapa)
    
    if quien == 1:
        opcion = input("Ingrese la casilla a jugar en el formato fila, columna: ")
        fila, columna = [int(x) for x in opcion.split(",")]
        
        # Verificar si la posición está dentro de los límites de la matriz
        if 0 <= fila < tamaño and 0 <= columna < tamaño:
            print("1. Iniciativa ")
            print("2. Proyecto")
            print("3. Cultura")
            opcion2 = input("¿Qué busca crear?: ")
            
            if opcion2 == "1":
                mapa[fila][columna] = 1
                os.system("cls")
                crear_juego(mapa, tamaño, 0)
            elif opcion2 == "2":
                mapa[fila][columna] = 2
                os.system("cls")
                crear_juego(mapa, tamaño, 0)
            elif opcion2 == "3":
                crear_cultura(mapa, fila, columna, tamaño)
            else:
                print("Seleccione una opción válida")
                os.system("cls")
                crear_juego(mapa, tamaño, 1)
        else:
            print("La posición está fuera de los límites de la matriz.")
            os.system("cls")
            crear_juego(mapa, tamaño, 1)
    else:
        tirarOponente(mapa, tamaño // 2)

def crear_cultura(mapa, fila, columna, tamaño):
    print("1. Expansión vertical")
    print("2. Expansión horizontal")
    opcion = input("Escoja una dirección: ")
    
    if opcion == "1":  # Expansión vertical
        for i in range(len(mapa)):
            if mapa[i][columna] in [6, 0]:
                mapa[i][columna] = 3

        os.system("cls")
        crear_juego(mapa, tamaño, 0)

    elif opcion == "2":  # Expansión horizontal
        for j in range(len(mapa)):
            if mapa[fila][j] in [6, 0]:
                mapa[fila][j] = 3
        
        os.system("cls")
        crear_juego(mapa, tamaño, 0)
    
    else:
        print("Opción no válida")
        os.system("cls")
        crear_juego(mapa, tamaño, 1)

# Función para gestionar el turno del oponente
def tirarOponente(mapa, tiradas):
    """
    E: Mapa, resultado del dado, estado de las piezas
    S: Actualización del tablero tras el turno del oponente
    R: Ninguna
    """
    
    for _ in range(tiradas):
        fila = random.randint(0, len(mapa) - 1)  
        columna = random.randint(0, len(mapa) - 1)  
        
        # Cambiar el valor en la posición seleccionada
        if mapa[fila][columna] in [0, 2, 3]:
            mapa[fila][columna] = 6
            tiradas -= 1
            print(f"El oponente usurpa la casilla ({fila}, {columna})")
    
    os.system("cls")
    crear_juego(mapa, len(mapa), 1)

def verificar_victoria(matriz):
    """
    Verifica si al menos una fila o columna de la matriz está compuesta por el mismo valor (1 o 2).

    E: matriz (lista de listas)
    S: True si al menos una fila o columna tiene todos sus elementos iguales a 1 o 2,
       False en caso contrario.
    """
    tamaño = len(matriz)

    # Verificar filas
    for fila in range(tamaño):
        victoria_indigenas = True
        victoria_usurpadores = True
        
        for elemento in matriz[fila]:
            if elemento != 2:
                victoria_indigenas = False
            if elemento != 6:
                victoria_usurpadores = False

        if victoria_indigenas:
            input("Victoria para los indigenas, INTRO ")
            os.system("cls")
            principal()
        elif victoria_usurpadores:
            input("Victoria para los usurpadores, INTRO ")
            os.system("cls")
            principal()

    # Verificar columnas
    for columna in range(tamaño):
        victoria_indigenas = True
        victoria_usurpadores = True
        
        for fila in range(tamaño):
            if matriz[fila][columna] != 2:
                victoria_indigenas = False
            if matriz[fila][columna] != 6:
                victoria_usurpadores = False

        if victoria_indigenas:
            print("Victoria para los indígenas")
            os.system("cls")
            principal()
        
        if victoria_usurpadores:
            print("Victoria para los usurpadores")
            os.system("cls")
            principal()
            

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


def instrucciones():
    os.system("cls")
    print("             INSTRUCCIONES DEL JUEGO           ")
    print(".                                              .\n")
    print("OBJETIVO DEL JUEGO\nEl objetivo es establecer iniciativas y proyectos culturales en el tablero\nmientras se defiende el territorio de los usurpadores. \nEl juego termina cuando uno de los dos bandos logra completar una fila o columna con \nsus proyectos consolidados o cuando los usurpadores dividen el territorio.\n")
    print("INICIAR EL JUEGO\nAl comenzar el juego se le pedira al jugador elegir el\ntamaño del tablero, por ejemplo 4 es un tablero 4x4.\nEl tablero se representará como \nuna matriz donde cada celda puede estar vacía, contener una iniciativa (I0), un proyecto (P), cultura (C), o ser usurpada (U).\n")
    print("TURNOS\nEl juego se juega en turnos alternos entre los pueblos\noriginarios (jugador) y los usurpadores (oponente). El jugador comienza primero.\n")
    print("PUEBLOS ORIGINARIOS\nEn tu turno, ingresa la casilla que deseas modificar en el formato fila,columna (por ejemplo, 1,2).\nDespués de seleccionar la casilla, se te presentarán tres opciones:\nIniciativa (I0): Marca la casilla como una iniciativa.\nProyecto (P): Marca la casilla como un proyecto.\nCultura (C): Expande la cultura en la dirección que elijas (vertical u horizontal).\n")
    print("USURPADORES\nEn el turno del oponente, este usurpará aleatoriamente varias casillas del tablero.\nSi un usurpador ocupa una iniciativa o un proyecto, estos serán destruidos.\n")
    print("VICTORIA\nSi todos los elementos de una fila o columna son iguales a P (Proyecto), el jugador gana.\nSi ocurre lo anterior pero con U (Usurpado), el usurpador gana.")
    input("Volver? INTRO ")
    principal()
    

def info_solarpunk():
    os.system("cls")
    print("                  INFORMACION SOBRE SOLARPUNK                  ")
    print("""
El Solarpunk es un movimiento cultural que propone un futuro optimista y conectando la naturaleza con la tecnología. Presenta\nrespuestas a los problemas medioambientales actuales, promoviendo un futuro sostenible\nmediante el uso de la tecnología. A diferencia de otros géneros tales como el cyberpunk\no el steampunk los cuales a menudo presentan visiones pesimistas, el Solarpunk se enfoca en la simbiosis\nentre el ser humano y la\nnaturaleza. Segun Cervera A. (2020), "el solarpunk es un movimiento que aspira a lograr cierta simbiosis entre hombre y naturaleza con el objetivo de despertar y \nprofundizar la sensibilidad ecológica del individuo y, en consecuencia, de la sociedad en general."

Este movimiento surgió en Brasil, 2012, relatos que exploraban un mundo sostenible, su popularidad crecio gracias al internet, \nespecialmente con el manifesto de Adam Flynn en 2014. 

Cuenta con unas variantes similares y relacionadas como el greenpunk, el cual busca una sociedad mas verde y justa y \nel biopunk que se centra mas en las implicaciones de la biotecnología y las éticas que conllevan. 
          """)


def info_pueblos():
    pass


def info_cabaga():
    pass


def links():
    pass


# MENU


def imprimir_banner_bienvenida():
    print("""
┌─────────────────────────────────────────────────────────────────────┐
│ ____                                          _                     │
│|  _ \ ___  ___ _   _ _ __   ___ _ __ __ _  __| | ___  _ ____  _____ │
│| |_) / _ \/ __| | | | '_ \ / _ \ '__/ _` |/ _` |/ _ \| '__\ \/ / __|│
│|  _ <  __/ (__| |_| | |_) |  __/ | | (_| | (_| | (_) | |   >  <\__ \│
│|_| \_\___|\___|\__,_| .__/ \___|_|_ \__,_|\__,_|\___/|_|  /_/\_\___/│
│  ___ _ __   |  _ \ _|_| ___(_)___| |_ ___ _ __   ___(_) __ _        │
│ / _ \ '_ \  | |_) / _ \/ __| / __| __/ _ \ '_ \ / __| |/ _` |       │
│|  __/ | | | |  _ <  __/\__ \ \__ \ ||  __/ | | | (__| | (_| |       │
│ \___|_| |_| |_| \_\___||___/_|___/\__\___|_| |_|\___|_|\__,_|       │
└─────────────────────────────────────────────────────────────────────┘    
          """)
    return "                          Menu Principal"


def imprimir_menu():
    print(" 1. Jugar")
    print(" 2. Instrucciones")
    print(" 3. Información Sobre Solarpunk")
    print(" 4. Información Sobre Pueblos Originarios")
    print(" 5. Información sobre el conflicto en Cabaga, Costa Rica")
    print(" 6. Links y Texto")
    print(" 7. Salir")


def es_opcion_valida(opcion):
    """
    Valida si la opcion es valida como 
    numero entero y si existe
    """
    if isinstance(opcion, int) == False:
        return False
    
    if opcion > 7 or opcion < 1:
        return False
    else:
        return True


#Función que muestra el menú principal
def principal():
    """
    Punto de Entrada del Programa
    Imprime el Menu y Da la Seleccion de
    la Opcion
    Si la opcion existe y es valida, retorna
    la funcion relacionada con dicha opcion
    """
    
    os.system('cls')
    print(imprimir_banner_bienvenida())
    imprimir_menu()
    print("")
    
    opcion = int(input("Seleccione una opcion: "))
    
    if es_opcion_valida(opcion) == False:
        input("Error01, INTRO ")
        principal()
    
    if opcion == 1:
        tamaño = input("Ingrese el tamaño del mapa: ")
        if 2 <= intNumero(tamaño) <= 12:
            iniciar_juego(intNumero(tamaño), 0,[])
        else:
            print("Seleccione un tamaño entre 2 y 12")
            os.system("cls")
            principal()
    
    if opcion == 2:
        instrucciones()
        
    if opcion == 3:
        info_solarpunk()
        
    if opcion == 4:
        info_pueblos()
        
    if opcion == 5:
        info_cabaga()
        
    if opcion == 6:
        links()
        
    if opcion == 7:
        print("Programa Cerrado")
        return 


# PRINCIPAL


principal()
