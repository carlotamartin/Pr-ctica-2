#Importamos librerías
import numpy as np
'''
El ejercicio es el mismo que el ejercicio1.py pero en
este python ve que es una variable de tipo
long en vez de una variable de tipo integer
'''
def aVeryBigSum(ar):
    suma = np.sum(ar)
    # Write your code here
    return print("La suma de todos los elementos del array es: "+ str(suma))
#Probamos la funcion
b = np.array([[ 1,  2],[ 3,  4],[ 5,  6],[ 7,  8],[ 9, 10],[11, 12]])

aVeryBigSum(b)

