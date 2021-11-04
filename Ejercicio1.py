#!/bin/python3
import math
import os
import random
import re
import sys
import numpy as np

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#
def simpleArraySum(ar):
    suma = np.sum(ar)
    # Write your code here
    return print("La suma de todos los elementos del array es: "+ suma)
#Probamos la funcion
b = np.array([[ 1,  2],[ 3,  4],[ 5,  6],[ 7,  8],[ 9, 10],[11, 12]])

print(simpleArraySum(b))

'''
if __name__ == '__main__':
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
        ar_count = int(input().strip())
        ar = list(map(int, input().rstrip().split()))
        result = simpleArraySum(ar)
        fptr.write(str(result) + '\n')
        fptr.close()
'''