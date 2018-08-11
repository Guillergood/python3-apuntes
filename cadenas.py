# Cosas con cadenas.

# En Python, las cadenas son objetos INMUTABLES.
# Una cadena de caracteres no se modificará jamás.
# Por ejemplo, cadena.lower() devolverá la cadena en minúsculas, pero 
# esta permanecerá tal y como estaba. Lo mismo con upper().

# Algunos ejemplos:
cadena = "Hola, mundo."
cad_min = cadena.lower()
cad_max = cadena.upper()
cad_cap = cadena.capitalize()
cad_tit = cadena.title()
cad_swap = cadena.swapcase()

print(cadena, "\n", cad_min, "\n", cad_max, "\n", 
      cad_cap, "\n", cad_tit, "\n", cad_swap, "\n",)

# ----------------------------------------------------------------------------
# Función len().
# La función len() devuelve la longitud de cualquier cosa que disponga de la
# misma, no sólo de las cadenas. 

print("La cadena mide ", len(cadena), " caracteres. \n")

# ----------------------------------------------------------------------------
# Pertenencia:
# Python permite comprobar si una cadena es parte de otra con el mecanismo in:
#
# Ejemplo:

cad = input("Introduce una cadena: ")
subcad = input("Introduce otra cadena: ")

if subcad in cad:
    print(subcad, " está contenida en ", cad, ".\n")
else:
    print(subcad, " no está contenida en ", cad, ".\n")

# ----------------------------------------------------------------------------
# Ocurrencia:
# Python también nos permite contar cuantas veces se repite una cadena dentro
# de otra:

# Nota: para añadir formato a una cadena se puede utilizar esta notación:
# "------ {} --- {} ... {} ---".format(arg0, arg1... argn)
#
# Se puede señalar el argumento que queremos en cada lugar, no tienen que estar
# ordenados:
# "------ {0} --- {2} ... {1} ---".format(arg0, arg1, arg2)
#
# Según el manual, es la que se debe priorizar. A partir de ahora, la usaremos.

print("La cadena contiene la letra A {} veces.\n".format(cad.count("a")))

# ----------------------------------------------------------------------------
# Reemplazo:
# Sí, también nos permite reemplazar caracteres:

print("Cadena nueva: {1}. \nCadena antigua:: {0}".format(cad, cad.replace("a", "Z")))

# ----------------------------------------------------------------------------
# Tipos de caracteres:
# Para comprobar de qué tipo es cada carácter, se puede usar el módulo string:
import string

# Este módulo dispone de métodos que devuelven cadenas con todos los
# caracteres de cada tipo. Por ejemplo, si queremos comprobar si un carácter es
# un número:
numero = "8"
letra = "a"

if numero in string.digits:
    print("{} es un número".format(numero))

if letra in string.ascii_letters:
    print("{} es una letra".format(letra))

# ----------------------------------------------------------------------------
# Secuenciar una cadena:
# Podemos dividir una cadena en una lista de cadenas. La división se hará 
# atendiendo a los espacios en blanco.
frase = "Álvaro Martínez Sevilla es una maravilla."
palabras = frase.split()

print(palabras[2])

# Para recomponerlas, podemos usar una cadena "pegamento" y el método join.
# La cadena pegamento puede estar vacía.

nueva_frase = " :D ".join(palabras)
print(nueva_frase)

# ----------------------------------------------------------------------------
# Y esto es todo por ahora sobre cadenas.





