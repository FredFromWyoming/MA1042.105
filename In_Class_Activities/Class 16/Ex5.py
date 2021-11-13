import pandas as pd  
import matplotlib.pyplot as plt

nombres = ['Poe', 'Lovecraft', 'García Márquez', 'Zafón', 'King', 'Asimov','Quiroga', 'Clarke', 'Tolkien', 'Dick']
novelas = ['El Silencio', 'Dagón', 'Cien años de Soledad', 'La sombra del viento', 'Eso', 'Yo Robot','Cuentos de Locura','2001 una odisea espacial', 'El Señor de los Anillos', 'Ubik']
vendidos = [100, 62, 88, 47, 130, 94, 23, 52, 110, 36]
año = [1849, 1937, 2014, "2020",  "--", 1992, 1937, 2008, 1973, 1982]
generos = ['terror', 'terror', 'realismo mágico', 'realismo mágico', 'terror', 'ciencia ficción', 'terror', 'ciencia ficción', 'fantasía', 'ciencia ficción']

autores2 = {'nombre': nombres, 'libro': novelas, 'muerte' : año, 'género': generos,'vendidos(miles)' : vendidos}

df_autores2 = pd.DataFrame(autores2)

plt.title("Títulos por género")
plt.ylabel("Cantidad de libros")
plt.grid(axis='y')

plt.hist(df_autores2['género'])
plt.show()