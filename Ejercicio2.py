

def compareTriplets(a,b):
    #Inicializamos las variables de resultado a 0.
    resultado_a = 0
    resultado_b = 0
    if a[0]<b[0]:
        resultado_b+=1
    else:
        resultado_a+=1
    if a[1]<b[1]:
        resultado_b+=1
    else:
        resultado_a+=1
    if a[2]<b[2]:
        resultado_b+=1
    else:
        resultado_a+=1

    resultado = [resultado_a, resultado_b]
    return print('El resultado es:' + str(resultado))

a = (45, 50,98)
b = (95,50,99)
compareTriplets(a,b)
