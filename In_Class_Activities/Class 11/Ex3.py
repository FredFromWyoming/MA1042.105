def producto2 (listA, listB):
    """Esta función multiplica elemento a elemento dos listas numéricas del mismo tamaño"""

    out = []

    if (len(listA) == len(listB)):
        for i in range(len(listA)):
            out += [ listA[i] * listB[i] ]
        return out

    else:

        return("Error: lists must be the same length")

    
    
print(producto2([1,2], [4,5,6]))
print(producto2([1,2,3], [4,5,6]))