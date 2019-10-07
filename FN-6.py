a=[4,3,2,1]
 
def suma_resta(lista):
    
    suma = 0
    aux = 0

    for i in range (len(lista)-1):
        
        resta = lista[i] - lista[i+1]
        suma = resta + aux
        aux = suma
    print("El total de la suma de las diferencias es " + str(suma))

suma_resta(a)

