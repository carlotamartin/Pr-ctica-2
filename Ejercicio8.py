#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
# 1. INTEGER s
# 2. INTEGER t
# 3. INTEGER a
# 4. INTEGER b
# 5. INTEGER_ARRAY apples
# 6. INTEGER_ARRAY oranges
#
'''
s : entero, punto de partida de la ubicación de la casa de Sam.
t : número entero, ubicación final de la ubicación de la casa de Sam.
a : entero, ubicación del manzano.
b : número entero, ubicación del naranjo.
manzanas : matriz de enteros, distancias a las que cada manzana cae del árbol.
naranjas : matriz de enteros, distancias a las que cada naranja cae del árbol
'''
def countApplesAndOranges(s, t, a, b, apples, oranges):
    #Inicializamos las variables resultado
    resultado_manzanas = 0
    resultado_naranjas=0
    #Empezamos a recorrer las manzanas
    for i in apples:
        resultado_manzanas += posicion_fruta(s, t, a, i)
    for i in oranges :
        resultado_naranjas += posicion_fruta(s, t, b, i)
    print('La cantidad de manzanas que caen en la casa de Sam son: '+resultado_manzanas)
    print('La cantidad de naranjas que caen en la casa de Sam son: '+resultado_naranjas)




punto_partida = 7
punto_final= 11
pos_manzano = 5
pos_naranjo = 15
manzanas = [-2, 2, 1]
naranjas= [5,-6]


def posicion_fruta (s, t, pos_arbol, pos_fruta):
    resultado = 0
    posicion= pos_arbol+pos_fruta
    if posicion>s and posicion<t:
        resultado +=1
    else:
        resultado= 0
    return resultado