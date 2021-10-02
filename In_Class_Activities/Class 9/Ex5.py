'''
Ejercicio 5: Escriba un programa que pida 5 calificaciones al usuario (desde luego con un ciclo) y usando la función media del ejercicio anterior calcule el promedio, y lo imprima en pantalla con el siguiente mensaje:

Hola, tu promedio final es:promedio_calculado
'''

def media(lista):
    sum = 0 
    count = 0

    for i in lista:
        sum += i
        count += 1

    return (sum/count)

list = []

for i in range (5):
    list += [float(input("Calificacion "+ str(i+1) + " : " ))]

print("Hola, tu promedio final es : " + str(media(list)))