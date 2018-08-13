# ----------------------------------------------------------------------------
# PYTHON 3 - APUNTES Y EJEMPLOS
# Ejemplo: baraja de cartas
# ----------------------------------------------------------------------------
# Autor: Juan Ocaña Valenzuela
# GitHub: patchispatch
# Este documento está regulado por la licencia GNU General Public License v3.0
# ----------------------------------------------------------------------------

# En este ejemplo veremos cómo aplicar elementos de azar a una lista de 
# "cartas", con la función choice. También podremos barajar, con shuffle.

# ----------------------------------------------------------------------------
# Para poder realizar este ejemplo, importamos los métodos necesarios desde
# random:
from random import choice
from random import sample
from random import shuffle

# Creamos nuestra baraja:
cartas = [chr(x) for x in range(0x1f0a1, 0x1f0af)]

#Veamos qué es esto:
print(cartas)

#Para escoger una carta al azar, utilizamos choice:
carta = choice(cartas)
print("Ha sacado la carta {}".format(carta))

# También podemos sacar varias a la vez:
muestra = sample(cartas, 5)
print("Las cartas escogidas son {}".format(muestra))

# Por último, barajamos:
shuffle(cartas)
print("\nBarajamos: {}".format(cartas))

# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------