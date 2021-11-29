#getViews([4,0,3.5,5,5,0])=([1,5])

#Ejercicio 3
def getIndNoViews(lista):
    out=[]
    for i in range (len(lista)):
        if (lista[i]==0):
            out.append(i)
    return (out)

print(getIndNoViews([4,0,3.5,5,5,0]))