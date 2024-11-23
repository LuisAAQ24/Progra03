# PROYECTO 3 DE TALLER DE PROGRAMACION
# SEMESTRE II 2024

import os
import random
import time

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
    
    # Inicializar variables
        fila = 0
        columna = 0
        coma_encontrada = False
    
        for caracter in opcion:
            if caracter == ',':
                coma_encontrada = True
            elif not coma_encontrada:
                fila = int(caracter)  # Construir el número de fila
            else:
                columna = int(caracter)  # Construir el número de columna


    # Verificar si la posición está dentro de los límites de la matriz
        if 0 <= fila < tamaño and 0 <= columna < tamaño:
            print("1. Iniciativa ")
            print("2. Proyecto")
            print("3. Cultura")
            opcion2 = input("¿Qué busca crear?: ")
            intopcion = int(opcion2)
            if 0 < intopcion < 3 :
                validacion(fila, columna, intopcion, mapa, tamaño)
            elif intopcion == 3:
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
        tirarOponente(mapa, tamaño//2)


def validacion(fila, columna, valor, mapa, tamaño):
    if mapa[fila][columna] in [1,2,4,5]:
        print("Ya existe algo en esta posición")
        time.sleep(1)
        os.system("cls")
        crear_juego(mapa, tamaño, 1)
    else:
        mapa[fila][columna] = valor
        os.system("cls")
        crear_juego(mapa, tamaño, 0)

def crear_cultura(mapa, fila, columna, tamaño):
    print("1. Expansión vertical")
    print("2. Expansión horizontal")
    opcion = input("Escoja una dirección: ")
    
    if opcion == "1":  # Expansión vertical

        for i in range(fila, -1, -1): 
            if mapa[i][columna] in [6, 0]:
                mapa[i][columna] = 3
            else:
                break 


        for i in range(fila + 1, len(mapa)): 
            if mapa[i][columna] in [6, 0]:
                mapa[i][columna] = 3
            else:
                break  

        os.system("cls")
        crear_juego(mapa, tamaño, 0)

    elif opcion == "2":  #horizontal

        for j in range(columna, -1, -1): 
            if mapa[fila][j] in [6, 0]:
                mapa[fila][j] = 3
            else:
                break  


        for j in range(columna + 1, len(mapa[fila])): 
            if mapa[fila][j] in [6, 0]:
                mapa[fila][j] = 3
            else:
                break 

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
 
    while tiradas > 0:
        
        for fila in range(len(mapa)):
            for columna in range(len(mapa)):
                if mapa[fila][columna] == 2:
                    mapa[fila][columna] = 6
                    print(f"El oponente usurpa la casilla ({fila}, {columna})")
                    tiradas -= 1
                    time.sleep(1)
        
        fila = random.randint(0, len(mapa) - 1)  
        columna = random.randint(0, len(mapa) - 1) 
        if mapa[fila][columna] in [0, 3]:
            mapa[fila][columna] = 6
            tiradas -= 1
            print(f"El oponente usurpa la casilla ({fila}, {columna})")
            time.sleep(1)
    
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
            time.sleep(2)
            os.system("cls")
            principal()
        elif victoria_usurpadores:
            input("Victoria para los usurpadores, INTRO ")
            time.sleep(2)
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
            time.sleep(2)
            os.system("cls")
            principal()
        
        if victoria_usurpadores:
            print("Victoria para los usurpadores")
            time.sleep(2)
            os.system("cls")
            principal()
            




def instrucciones():
    os.system("cls")
    print("             INSTRUCCIONES DEL JUEGO           ")
    print(".                                              .\n")
    print("OBJETIVO DEL JUEGO\nEl objetivo es establecer iniciativas y proyectos culturales en el tablero\nmientras se defiende el territorio de los usurpadores. \nEl juego termina cuando uno de los dos bandos logra completar una fila o columna con \nsus proyectos consolidados o cuando los usurpadores dividen el territorio.\n")
    print("INICIAR EL JUEGO\nAl comenzar el juego se le pedira al jugador elegir el\ntamaño del tablero, por ejemplo 4 es un tablero 4x4.\nEl tablero se representará como \nuna matriz donde cada celda puede estar vacía, contener una iniciativa (I0), un proyecto (P), cultura (C), o ser usurpada (U).\n")
    print("TURNOS\nEl juego se juega en turnos alternos entre los pueblos\noriginarios (jugador) y los usurpadores (oponente). El jugador comienza primero.\n")
    print("PUEBLOS ORIGINARIOS\nEn tu turno, ingresa la casilla que deseas modificar en el formato fila,columna (por ejemplo, 1,2).\nDespués de seleccionar la casilla, se te presentarán tres opciones:\nIniciativa (I0): Marca la casilla como una iniciativa.\nProyecto (P): Marca la casilla como un proyecto.\nCultura (C): Expande la cultura en la dirección que elijas (vertical u horizontal).\n")
    print("USURPADORES\nEn el turno del oponente, este usurpará aleatoriamente varias casillas del tablero.\nSi un usurpador ocupa una iniciativa o un proyecto, estos serán destruidos.\n")
    print("VICTORIA\nSi todos los elementos de una fila o columna son iguales a P (Proyecto), el jugador gana.\nSi ocurre lo anterior pero con U (Usurpado), el usurpador gana.\n")
    print("VICTORIA\nSi todos los elementos de una fila o columna son iguales a P (Proyecto), el jugador gana.\nSi ocurre lo anterior pero con U (Usurpado), el usurpador gana.\n")
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
    input("Volver? INTRO ")
    principal()


def info_pueblos():
    os.system("cls")
    print("          PUEBLOS ORIGINARIOS          ")
    print("""
Los pueblos indígenas son grupos sociales y culturales que mantienen vínculos ancestrales con \nsus territorios y recursos naturales. Se estima que hay aproximadamente 476 millones de personas indígenas en el mundo, lo que representa \nalrededor del 6% de la población global, aunque constituyen cerca del 19% de las personas que viven en \ncondiciones de extrema pobreza.\n
Segun Ivers, L:
"Los pueblos indígenas a menudo carecen de reconocimiento formal de sus tierras, \nterritorios y recursos naturales, suelen ser los últimos en recibir inversiones \npúblicas en servicios básicos e infraestructura y enfrentan múltiples obstáculos para participar plenamente en la economía formal, obtener acceso a la justicia y ser parte de \nlos procesos políticos y la toma de decisiones." (s.f.)\n
En las últimas décadas, ha habido un creciente reconocimiento internacional de los derechos indígenas, reflejado en \ninstrumentos como la Declaración de las Naciones \nUnidas sobre los Derechos de los Pueblos Indígenas (UNDRIP) y el Acuerdo de Escazú.\n
Aunque los pueblos originarios / indigenas enfrentan numerosos desafos en la actualdad, tambien son protectores esenciales de la \nbiodiversidad, ademas de apoortar gran parte de algunas culturas en diiversos pases.
          """)
    input("Volver? INTRO ")
    principal()


def info_cabagra():
    os.system("cls")
    print("        INFORMACION SOBRE EL CONFLICTO DE CABAGRA, CR          ")
    print("""
En 2020 el Consejo de Mayores de Cabagra denuncio la entrada de personas no indigenas, armadas en areas recuperadas por las\ncomunidades indigenas, lo que ha generaado preocupacion por la escala de violencia. 

Segun Mora, A:
"La denuncia la realizó el Frente Nacional de Pueblos Indígenas (FRENAPI) que señaló mediante un comunicado que la tarde de\neste domingo 23 de febrero, el Consejo de Mayores del territorio de Cabagra informó sobre una movilización de personas no indígenas (sikuas, que es el vocablo con el que los pueblos indígenas se refieren al resto de la población) que entraron armados\na las zonas de Térraba, Crun D'bonn y Cabagra en Palmira, donde se encuentran las últimas tierras recuperadas por las personas indígenas." (s.f.)

Este conflicto no es nada nuevo en estos territorios y tampoco en el pais en general, se extiende a todas las zonas indigenas\ndel pais. "Las tierras de estos territorios son inalienables e imprescriptibles, no transferibles\ny exclusivas para las comunidades indígenas que las habitan" y que "los no indígenas no podrán alquilar, arrendar, comprar o de cualquier otra manera\nadquirir terrenos o fincas comprendidas dentro de estas reservas" (Ley ndigenaa 6172 de 1977, Articulo 3)

Segun Mora, A:
"Sin embargo, durante años dichas tierras han sido ocupadas por personas no indígenas que se hicieron de las terrenos de\ndiversas formas, ya sea poseyéndolas a la fuerza o comprándolas a pesar de que esto sea ilegal.\nEsto ha generado, principalmente después de que los pueblos indígenas decidiesen unirse para recuperar sus territorios (en el proceso que llaman "recuperación de tierras") una\nescalada en la violencia en la zona que llegó incluso a provocar el homicidio del líder bribri Sergio Rojas Ortíz, a inicios del año pasado." (s.f.)

          """)
    input("Volver? INTRO ")
    principal()


def links():
    os.system("cls")
    print("              BIBLBIOGRAFIA Y OTROS LINKS          ")
    print("1.")
    print("Cervera, A. (2020, diciembre 27). Solarpunk: Dibujando un futuro positivo para el planeta -. SIMBIOTIA. \nhttps://www.simbiotia.com/solarpunk/\n")
    print("2.")
    print("Mora, A. (s/f). Conflictos en territorios indígenas salen de Salitre y llegan también a Cabagra. \nRecuperado el 23 de noviembre de 2024, de https://delfino.cr/2020/02/conflictos-en-territorios-indigenas-salen-de-salitre-y-llegan-tambien-a-cabagra\n")
    print("3.")
    print("Ivers, L. (s/f). Pueblos indígenas: Panorama general [Text/HTML]. World Bank. \nRecuperado el 23 de noviembre de 2024, de https://www.bancomundial.org/es/topic/indigenouspeoples\n")
    input("Volver? INTRO ")
    principal()
    

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
        if 3 <= int(tamaño) <= 12:
            iniciar_juego(int(tamaño), 0,[])
        else:
            print("Seleccione un tamaño entre 3 y 12")
            time.sleep(1)
            os.system("cls")
            principal()
    
    if opcion == 2:
        instrucciones()
        
    if opcion == 3:
        info_solarpunk()
        
    if opcion == 4:
        info_pueblos()
        
    if opcion == 5:
        info_cabagra()
        
    if opcion == 6:
        links()
        
    if opcion == 7:
        print("Programa Cerrado")
        return 


# PRINCIPAL


principal()
