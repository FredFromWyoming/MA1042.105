#Ejercicio 6: Defina una función llamada factores, que dado un entero n regrese la lista de todos los divisores de n.
def factores (n):
    list = []

    for i in range (1,n+1):
        if (n%i == 0):
            list += [i]

    return(list)