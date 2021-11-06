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

def mostrar_ganador(n, inicia_juego, segundo_juego):
    if n == 1:
        print(inicia_juego + 'no puede hacer ningun movimiento y pierde el juego.')
    elif n==2:
        n= n-2
        print(inicia_juego + 'elimina piedras del tablero de juego y gana el juego.')
    elif n==3:
        n=n-2
        print (inicia_juego + ' elimina piedras en su primer movimiento, dejando piedra en el tablero y ganando el juego.')
    elif n==4:
        n=n-3
        print (inicia_juego + ' elimina piedras en su primer movimiento, dejando piedra en el tablero y ganando el juego.')
    elif n==5:
        n= n-5
        print(inicia_juego + ' elimina piedras del tablero de juego y gana el juego.')
    elif n==6:
        n=n-6
        print (inicia_juego + ' elimina piedras en su primer movimiento, dejando piedra en el tablero y ganando el juego.')
    elif n==7:
        '''
        Existen tres opciones pero en todas va a ganar segundo_juego
        Las tres opciones son:
        Eliminar 2 piedras, dejando 5 piedras en el tablero. P2 luego quita piedras, ganando el juego.
        Eliminar 3 piedras , dejando 4 piedras en el tablero. P2 luego quita piedras, dejando piedra dejada en el tablero y ganando el juego.
        Eliminar 5 piedras, dejando3 piedras en el tablero.P2 luego quita el piedras restantes y gana el juego.
        '''
        n=n-2
        print(inicia_juego+' elimina dos piedras, dejando '+ n+ ' en el tablero.')
        n=n-5
        print(segundo_juego+ ' luego quita las piedras, ganando el juego.')