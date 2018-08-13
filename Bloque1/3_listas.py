# ----------------------------------------------------------------------------
# PYTHON 3 - APUNTES Y EJEMPLOS
# Listas
# ----------------------------------------------------------------------------
# Autor: Juan Ocaña Valenzuela
# GitHub: patchispatch
# Este documento está regulado por la licencia GNU General Public License v3.0
# ----------------------------------------------------------------------------

# Veremos qué es una lista, por qué son tan útiles y varios conceptos 
# relacionados, como los índices, la inserción y el borrado, el acceso a 
# sus elementos, y la iteración.

# ----------------------------------------------------------------------------
# Sintaxis.

# La lista es un elemento contenedor muy común. Es modificable, a diferencia 
# de las cadenas.
# Comencemos creando una lista:
lista = list("Abracadabra")

# Esto es equivalente a declararla así:
lista = ['A', 'b', 'r', 'a', 'c', 'a', 'd', 'a', 'b', 'r', 'a']

# Dispondríamos en este caso de una lista de 11 elementos.

# ----------------------------------------------------------------------------
# Índices.

# Para acceder a cada elemento de una lista, necesitamos conocer. Cada 
# elemento tiene asociado un índice, comenzando desde 0. En nuestra lista:
#
# A|b|r|a|c|a|d|a|b|r|a
# 0|1|2|3|4|5|6|7|8|9|10

# Vamos a cambiar la A mayúscula por una minúscula:
lista[0] = 'a'

# Python también permite el uso de índices negativos, para empezar por el
# final:
b = lista[-3]  # b incluye el carácter 'b'

# Podemos extraer sub-cadenas indicando un rango, de la siguiente manera:
sub_lista = lista[:4]

# sub_lista contiene los valores 0, 1, 2 y 3 de lista, es decir, desde el 
# principio (incluido) hasta el 4 (excluido). 
# Si quisiésemos guardar desde la posición 5 hasta el final:
sub_lista_2 = lista[5:]

# Y si quisiésemos, por ejemplo, de la 4 a la 6, esta última incluida:
sub_lista_3 = lista[4:7]

# De esta sintaxis podemos sacar las siguientes conclusiones:
# Primer argumento: inicio, incluido en la selección. Vacío = principio.
# Segundo argumento: final, excluido de la selección. Vacío = final.

# También podemos utilizar un paso entre elementos, utilizando un tercer 
# argumento:
# Esto guardará en la variable los elementos del 1 hasta el final separados 
# por otros 3, es decir, ['b', 'c', 'a', 'a']
sub_lista_4 = lista[1::3]

# Se pueden reemplazar varios elementos a la vez, pero deben ser de igual
# longitud:
lista[1:4] = "6"

# Por último, podemos eliminar elementos. La longitud de la lista variará,
# por supuesto:
del lista[0]

# Y podemos borrar varios elementos a la vez:
del lista[:3]

# ----------------------------------------------------------------------------
# Valores.

# Las listas también permiten el uso de in y count(), como las cadenas.
# Además, es posible eliminar un elemento sin saber su índice:
lista.remove("a")

# O eliminar la lista entera:
while " " in lista:
    lista.remove(" ")

# También podemos insertar y sacar cosas del final de la lista, utilizándola
# a modo de pila:
lista.append("h")
valor = lista.pop()  # valor contiene "h".

# Podemos insertar en el lugar que queramos:
lista.insert(2, "f")

# Y podemos "pegar" otra lista al final:
lista.extend(sub_lista)

# ----------------------------------------------------------------------------
# Continuará...