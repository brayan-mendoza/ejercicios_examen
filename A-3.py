#cuenta de positivos/suma de negativos

def conteo_Suma(arreglo):
    contadorP = 0
    sumaN = 0
    for i in range(len(arreglo)):
        if arreglo[i] > 0:
            contadorP = contadorP + 1
        else:
            sumaN = arreglo[i] + sumaN
            
    print("El total de numeros positivos es: " + str(contadorP))
    print("La suma de numeros negativos es: " + str(sumaN))

lista = [1,2,3,4,5,6,-11,-12,-13,-14,-15]

conteo_Suma(lista)

