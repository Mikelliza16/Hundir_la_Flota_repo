import numpy as np

from utils import tablero
import random

def tablero():
    tablero = np.full((10,10), " ")
    return tablero

tablero_jugador = tablero()
tablero_rival = tablero()
print("Tablero_jugador")
print(tablero_jugador)
print("___________________________________________")
print("Tablero_rival")
print(tablero_rival)


#FUNCIÓN PARA CREAR BARCOS

import random

def crear_barco(eslora, tamaño=10): 
    fila = random.randint(0, tamaño - 1)
    columna = random.randint(0, tamaño - 1)
    direccion = random.choice(["horizontal", "svertical"])
    barco = []

    for i in range(eslora):
        if direccion == "horizontal" and columna + eslora <= tamaño:
            barco.append((fila, columna + i))
        elif direccion == "vertical" and fila + eslora <= tamaño:
            barco.append((fila + i, columna))
        else:
            # Si el barco se sale del tablero, se repite
            return crear_barco(eslora, tamaño)
    return barco

