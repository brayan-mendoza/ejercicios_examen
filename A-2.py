#programa que indique que numeros de una 
# lista, son divisibles por un numero dado

lista1 = [0,2,4,6,1,9]

def divisible(lista,divisor):

    for i in range (0,len(lista)):
        if lista[i] != 0:
           if lista[i] % divisor == 0:
               print("resultado " + str(lista[i]))

numero=int(input("introduzca el valor del divisor: "))      
divisible(lista1,numero)

