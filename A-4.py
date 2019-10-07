alumno1 = [9, 8, 7, 5, 2, 10]
alumno2 = [5,5,5,5,5]
alumno3 = [0,1,2]
alumno4 = [4,9,4,5,7,8]
alumno5 = [1,1,1,1,]
def porcentaje(alumnos):
    sum = 0
    calificacion = 0
    a = 0
    for i in range (len(alumnos)):
        sum = alumnos[i]+ sum
        calificacion = sum / len(alumnos)
    if calificacion >= 6 :
        return (a + 1)
    else:
        return a

porcentaje(alumno1)
porcentaje(alumno2)
porcentaje(alumno3)
porcentaje(alumno4)
porcentaje(alumno5)
aprobados= ((porcentaje(alumno1) + porcentaje(alumno2) + porcentaje(alumno3) + porcentaje(alumno4) + porcentaje(alumno5)) / 5 ) * 100
reprobados = 100 - aprobados 
print("El porcentaje de aprobados es: " + str(aprobados) + "%")
print("El porcentaje de aprobados es: " + str(reprobados) + "%")