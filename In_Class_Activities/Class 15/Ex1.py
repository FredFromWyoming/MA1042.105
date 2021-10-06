quijote ="""En esto descubrieron treinta o cuarenta molinos de viento que hay en aquel campo, y así como don Quijote los vió, dijo a su escudero: 
-La ventura va guiando nuestras cosas mejor de lo que acertáramos a desear; porque ves allí, amigo Sancho Panza, donde se descubren treinta o poco más desaforados gigantes con quien pienso hacer batalla, y quitarles a todos las vidas, con cuyos despojos comenzaremos a enriquecer: que esta es buena guerra, y es gran servicio de Dios quitar tan mala simiente de sobre la faz de la tierra.

-¿Qué gigantes?-dijo Sancho Panza.

-Aquellos que allí ves-respondió su amo-, de los brazos largos, que los suelen tener algunos de casi dos leguas.

-Mire vuestra merced-respondió Sancho-, que aquellos que allí se parecen no son gigantes, sino molinos de viento, y lo que en ellos parecen brazos son las aspas, que volteadas del viento hacen andar la piedra del molino.

-Bien parece-respondió don Quijote- que no estás cursado en esto de las aventuras; ellos son gigantes, y si tienes miedo quítate de ahí, y ponte en oración en el espacio que yo voy a entrar con ellos en fiera y desigual batalla.

Y diciendo esto, dio de espuelas a su caballo Rocinante, sin atender a las voces que su escudero Sancho le daba, advirtiéndole que sin duda alguna eran molinos de viento, y no gigantes aquellos que iba a acometer. Pero él iba tan puesto en que eran gigantes, que ni oía las voces de su escudero Sancho, ni echaba de ver, aunque estaba ya bien cerca, lo que eran; antes iba diciendo en voces altas:

-Non fuyades, cobardes y viles criaturas, que un solo caballero es el que os acomete.

Levantose en esto un poco de viento y las grandes aspas comenzaron a moverse, lo cual visto por don Quijote, dijo:

-Pues aunque mováis más brazos que los del gigante Briareo, me lo habéis de pagar.

Y en diciendo esto, y encomendándose de todo corazón a su señora Dulcinea, pidiéndole que en tal trance le socorriese, bien cubierto de su rodela, con la lanza en ristre, arremetió a todo el galope de Rocinante, y embistió con el primer molino que estaba delante; y dándole una lanzada en el aspa, la volvió el viento con tanta furia, que hizo la lanza pedazos, llevándose tras sí al caballo y al caballero, que fue rodando muy maltrecho por el campo. Acudió Sancho Panza a socorrerle a todo el correr de su asno, y cuando llegó, halló que no se podía menear, tal fue el golpe que dio con él Rocinante"""

import matplotlib.pyplot as plt

alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","Ñ"]

letterCount = {}
inverseCount = []

for i in alphabet:
    letterCount [i] = quijote.upper().count(i)

    for h in range (letterCount[i]):
        inverseCount.append(i)

#Eexercicio 2
print("Ecercicio 2: " + str(letterCount))

#Exercicio 1
plt.title("Exercicio 1")
plt.grid(True)
plt.hist(inverseCount, bins = len(alphabet) )
plt.show()  