#EJERCICIO: COMPARA LOS PROBLEMAS
# a y b son dos arrays que tienen cada uno tres elementos en el interior
def compareTriplets(a, b):
    resultado = []
    resultado_a = 0
    resultado_b = 0
    #Inicializamos un bucle que recorra las dos listas y las podamos comparar
    for i in a:
        for j in b:
            if i>j:
                resultado_a +=1
                resultado.insert(0, resultado_a )
            elif i<j:
                resultado_b += 1
                resultado.insert(1, resultado_b)
    return resultado
#Probamos el método
a = (45, 50,99)
b= (95,50,99)
print (compareTriplets(a,b))
