def producto1 (listA, listB):
    """Esta función multiplica elemento a elemento dos listas numéricas del mismo tamaño"""

    out = []

    if (len(listA) == len(listB)):
        for i in range(len(listA)):
            out += [ listA[i] * listB[i] ]
    else:
        out = [0]

    return (out)
    
print(producto1([1,2,3], [4,5,6]))