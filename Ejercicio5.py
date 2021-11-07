def gameOfStones(n):
    if n<1 or n>7:
        print ('No se puede jugar al juego')
    inicia_juego = 'P1'
    segundo_juego='P2'
    if n == 1:
        print(inicia_juego + 'no puede hacer ningun movimiento y pierde el juego.')
        print('P1 gana')
    elif n==2:
        n= n-2
        print(inicia_juego + 'elimina piedras del tablero de juego y gana el juego.')
        print('P1 gana')

    elif n==3:
        n=n-2
        print (inicia_juego + ' elimina piedras en su primer movimiento, dejando piedra en el tablero y ganando el juego.')
        print('P1 gana')
    elif n==4:
        n=n-3
        print (inicia_juego + ' elimina piedras en su primer movimiento, dejando piedra en el tablero y ganando el juego.')
        print('P1 gana')
    elif n==5:
        n= n-5
        print(inicia_juego + ' elimina piedras del tablero de juego y gana el juego.')
        print('P1 gana')
    elif n==6:
        n=n-6
        print (inicia_juego + ' elimina piedras en su primer movimiento, dejando piedra en el tablero y ganando el juego.')
        print('P1 gana')
    elif n==7:
        '''
        Existen tres opciones pero en todas va a ganar segundo_juego
        Las tres opciones son:
        Eliminar 2 piedras, dejando 5 piedras en el tablero. P2 luego quita piedras, ganando el juego.
        Eliminar 3 piedras , dejando 4 piedras en el tablero. P2 luego quita piedras, dejando piedra dejada en el tablero y ganando el juego.
        Eliminar 5 piedras, dejando3 piedras en el tablero.P2 luego quita el piedras restantes y gana el juego.
        '''
        n=n-2
        print(inicia_juego+' elimina dos piedras, dejando '+ str(n)+ ' en el tablero.')
        n=n-5
        print(segundo_juego+ ' luego quita las piedras, ganando el juego.')
        print('P2 gana')

gameOfStones(9)