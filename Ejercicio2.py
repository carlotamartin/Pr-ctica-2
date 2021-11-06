def compareTriplets(a, b):
    #Inicializamos las variables de resultado a 0.
    resultado_a = 0
    resultado_b = 0
    #Calculamos la longitud de la lista de a e inicializamos a 0 el índice
    longitud = len(a)
    indice = 0
    #Ahora creamos un bucle que se repita mientras la longitud sea mayor al indice.
    # En cada repetición iremos añadiendo uno al índice.
    while indice < longitud:
        item = a[indice]
        if item > b[indice]:
            resultado_a+=1
        elif item < b[indice]:
            resultado_b+=1
    resultado = [resultado_a, resultado_b]
    return print('El resultado es:' + str(resultado))

#Probamos el método
a = (45, 50,98)
b = (95,50,99)
compareTriplets(a,b)



