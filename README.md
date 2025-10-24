# Hundir_la_Flota_repo

Este proyecto es una versión  del clásico juego Hundir a la Flota, desarrollada en Python utilizando NumPy.
Permite crear tableros, colocar barcos de forma aleatoria, realizar disparos y gestionar los turnos entre el jugador y el rival.

🧩 Estructura del proyecto

El proyecto se divide en dos archivos principales:

main.py → Contiene el flujo principal del juego (tableros, barcos, disparos y turnos).

utils.py → Contiene las funciones auxiliares para crear tableros, generar barcos, colocarlos y disparar.

⚙️ Funcionalidades principales

crear_tablero(tamaño)
Crea un tablero de juego (por defecto 10x10) relleno con el carácter "_" usando NumPy.

crear_barco(eslora)
Genera de forma aleatoria la lista de posiciones (coordenadas) de un barco según su tamaño (eslora).

colocar_barco(barco, tablero)
Coloca un barco en el tablero, marcando las posiciones con "O".

disparar(casilla, tablero)
Simula un disparo a una casilla del tablero.

Si acierta en un barco ("O"), se marca como "X" → Tocado.

Si falla ("_"), se marca como "A" → Agua.

colocar_barcos(tablero)
Coloca todos los barcos de forma aleatoria en el tablero sin solaparlos (6 barcos en total):

3 barcos de eslora 2

2 barcos de eslora 3

1 barco de eslora 4

Sistema de turnos
Permite alternar los disparos entre el jugador y el rival.
Cada disparo modifica el tablero correspondiente, y el juego continúa hasta que todos los barcos de un jugador han sido hundidos.