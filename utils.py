import numpy as np

import random

def tablero():
    tablero = np.full((10,10), " ")
    return tablero


def crear_barco(eslora, tamaño=10): 
    fila = random.randint(0, tamaño - 1)
    columna = random.randint(0, tamaño - 1)
    direccion = random.choice(["horizontal", "vertical"])
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


def colocar_barco(barco, tablero):
    for fila, columna in barco:
        tablero[int(fila)][int(columna)] = "O"
    return tablero


def disparar(tablero, fila, columna):
   if tablero[fila,columna] == "O":
      print("Tocado")
      tablero[fila,columna] = "X"
      return tablero
   else:
      print("AGUA!")
      tablero[fila,columna] = "A"
      return tablero
   
def mostrar_tablero(tablero, nombre):
    print(f"\nTablero de {nombre}:")
    for fila in tablero:
        print(" ".join(fila))