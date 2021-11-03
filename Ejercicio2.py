#EJERCICIO: COMPARA LOS PROBLEMAS
# a y b son dos arrays que tienen cada uno tres elementos en el interior
def compareTriplets(a, b):
    resultado = []
    #Inicializamos un bucle que recorra las dos listas y las podamos comparar
    for i in a:
        for j in b:
            if i>j:
                resultado[0]+=1
            elif i<j:
                resultado[1]+=1
    return resultado
#Probamos el método
a = (45, 50,99)
b= (95,50,99)
print (compareTriplets(a,b))
