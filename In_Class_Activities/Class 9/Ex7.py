#Ejercicio 7: Usando factores, defina una función llamada es_primo que dado un entero n regrese True si n es primo, y False en caso contrario (recuerde que un número es primo si sus únicos divisores son 1 y el mismo número).
def factores (n):
    list = []

    for i in range (1,n+1):
        if (n%i == 0):
            list += [i]

    return(list)

def es_primo (n):
    if (len(factores(n))==2):
        return True
    else:
        return False