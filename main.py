from utils import tablero, crear_barco, colocar_barco, mostrar_tablero


#Crear - imprimir tablero
tablero_jugador = tablero()
tablero_rival = tablero()


#Crear - imprimir barcos
barcos_jugador = [crear_barco(2, tamaño=10),
                  crear_barco(2, tamaño=10),
                  crear_barco(2, tamaño=10),
                  crear_barco(3, tamaño=10),
                  crear_barco(3, tamaño=10),
                  crear_barco(4, tamaño=10),]

for b in barcos_jugador:
    colocar_barco(b, tablero_jugador)

# === CREAR BARCOS RIVAL ===
barcos_rival = [crear_barco(2, tamaño=10),
                crear_barco(2, tamaño=10),
                crear_barco(2, tamaño=10),
                crear_barco(3, tamaño=10),
                crear_barco(3, tamaño=10),
                crear_barco(4, tamaño=10),]

for b in barcos_rival:
    colocar_barco(b, tablero_rival)

#Imprimir - tableros con barcos:
print("Tablero del Jugador:")
print(tablero_jugador)
print("________________________________________")
print("Tablero del Rival:")
print(tablero_rival)
print("________________________________________")


# Inicio del juego:

turno = 1  # 1 = jugador, 2 = rival

print("\n¡Comienza a jugar! ¡Jugador te toca a tí!")

while True:
    print(f"\nTurno del jugador {turno}")
# Disparar
    fila = int(input("Fila (0-9): "))
    columna = int(input("Columna (0-9): "))

    if turno == 1:  # Turno del jugador
        
        if tablero_rival[fila][columna] == "O":
            print("¡Tocado!")
            tablero_rival[fila][columna] = "X"
        else:
            print("¡Agua!")
            tablero_rival[fila][columna] = "A"

        # Comprobar si el jugador ha ganado
        barcos_restantes = any("O" in f for f in tablero_rival)
        if not barcos_restantes:
            print("\n¡El jugador ha ganado la partida!")
            break

        turno = 2  # Pasa al rival

    else:  # Turno del rival
       
        if tablero_jugador[fila][columna] == "O":
            print("¡Tocado!")
            tablero_jugador[fila][columna] = "X"
        else:
            print("¡Agua!")
            tablero_jugador[fila][columna] = "A"

        # Comprobar si el rival ha ganado
        barcos_restantes = any("O" in f for f in tablero_jugador)
        if not barcos_restantes:
            print("\n¡El rival ha ganado la partida!")
            break

        turno = 1  # Vuelve al jugador

    mostrar_tablero(tablero_jugador, "Jugador")
    mostrar_tablero(tablero_rival, "Rival")