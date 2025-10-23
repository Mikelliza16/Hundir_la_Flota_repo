import numpy as np

tablero = np.full((10,10), " ")
print(tablero)




#1. Diseñar el tablero
import numpy as np
def tablero():
    tablero = np.full((10,10), " ")
    return tablero
#Para pintar los barcos
def colocar_barco(tablero, lista):
    for barco in lista:
        #Para acceder al barco
        print(barco)
        for posicion in barco:
            #Para que me saque cada posicon de los barcos
            print(posicion)
            #Reemplazar los " " por "\
            tablero[posicion] = "0"
    return tablero
'''
#Barcos aleatorios
def validar_posicion_aleatoria(tablero, inicio_fila, inicio_columna, eslora, direccion):
    #Verifica si un barco cabe y no se superpone en las coordenadas generadas.
    tamaño = tablero.shape[0]
    coordenadas = []
    for i in range(eslora):
        # 1. Calcular la coordenada de la parte del barco
        if direccion == 'H':  # Horizontal
            fila, columna = inicio_fila, inicio_columna + i
        else:  # Vertical
            fila, columna = inicio_fila + i, inicio_columna
        # 2. Comprobar límites
        if not (0 <= fila < tamaño and 0 <= columna < tamaño):
            return False, []
        # 3. Comprobar superposición
        if tablero[fila, columna] != "_":
            return False, [] # La casilla no está vacía
        coordenadas.append((fila, columna))
    return coordenadas
'''
def disparar(tablero, fila, columna):
    if tablero[fila, columna] == "0":
        tablero[fila, columna] = ":calavera_y_tibias_cruzadas:"
        print(tablero)
        print("Tocado")
    elif tablero[fila, columna] == "X":
        tablero[fila, columna] = "•"
        print(tablero)
        print("Agua")
    elif tablero[fila, columna] == "•":
        return disparar(tablero, fila, columna)
    else:
        print("Esa poscion no existe")
    print(tablero)
#CABE NO CABE
#TURNOS con while == True hasta que uno haya pisado todos los barcos == FALSE se acaba
14:44
import numpy as np
#Importar funciones
from utils import tablero
from utils import colocar_barco
from utils import dispararos
tablero_player_01 = tablero()
tablero_player_02 = tablero()
print("Tablero Player 01\n", tablero_player_01)
print("Tablero Player 02\n", tablero_player_02)
#Las posiciones de los barcos
lista_barcos_player_01 = [[(1, 4), (1, 5), (1, 6)], [2, 3]]
#Los tableros con los barcos
tabero_player_01_barcos = colocar_barco(tablero_player_01, lista_barcos_player_01)
fila = int(input("Añade el numero de la fila de 0 a 9: "))
columna = int(input("Añade el numero de la columna de 0 a 9: "))
tablero_player_01 = disparar()
#Barco horizontalmente
tablero_player_01[0][0] = "O"
tablero_player_01[0][1] = "O"
tablero_player_01[0][2] = "O"
#Barco verticalmente
tablero_player_01[3][0] = "O"
tablero_player_01[4][0] = "O"
tablero_player_01[5][0] = "O"
