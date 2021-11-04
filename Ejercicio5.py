def gameOfStones(n):
    #Inicializamos las variables de las punturaciones de cada jugador a 0
    puntos_P1 = 0
    puntos_P2=0

    #Empieza 
    if puntos_P1>puntos_P2:
        ganador = puntos_P1
    else:
        ganador = puntos_P2

    return ganador