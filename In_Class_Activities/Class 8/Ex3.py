#Ex3

lista_prueba = [22, 44, 55, 57, 42, 87, 123, -90, 12, -118, 1000, 500, 71, -88]
out = []

for i in lista_prueba:
    if (i % 4 == 0):
        out += [i]

print(out)