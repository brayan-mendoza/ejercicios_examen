# utlizando ciclos (loops) dinujar un triangulo de asteriscos
def triangulo(altura):
    for numero_linea in range(altura):
        espacios = altura - numero_linea - 1
        print("", espacios)
        asteriscos = 1 + numero_linea * 2
        print (" " * espacios + "*" * asteriscos)


alt = int(input("introduce la altura: "))
triangulo(alt)