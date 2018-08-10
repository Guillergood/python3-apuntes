#Cosillas del libro para probar

# #Hola mundo
# print ("Hola wapa kiere seso")

# #Lectura de entrada estandar
# informacion = input("Introduzca lo que sea: ")
# print("Ha introducido: ", informacion)

#Comparaciones:

# Vamos a comparar dos números:

# numero1 = input("Introduzca un número: ")
# numero2 = input("Introduzca otro número: ")

# resultado = numero1 < numero2

# print (numero1, "<", numero2, ": ", resultado)

#Resultado será True, pues esto compara cadenas de caracteres. Para comparar
#números, debemos asignar tipos a las variables o su contenido:

# # Una forma de hacerlo:
# numero1 = input("Introduzca un número: ")
# numero1 = int(numero1) 

# #Otra forma de hacerlo, más corta, pero menos legible y más difícil de
# #depurar:
# numero2 = int(input("Introduzca otro número: "))



# Si queremos que nuestro programa maneje la excepción si el usuario introduce 
# algo que no es un entero, debemos importar el módulo sys

import sys

# Ahora disponemos de una variable sys, que apunta al módulo.
# Este módulo contiene una función exit(). 
# Nuestra intención es:
# Si el usuario introduce un número, continuar.
# Si se produce una excepción, escribir un mensaje y salir.

# La sección crítica (la que puede producir una excepción) la 
# escribimos en el bloque try:
# try:
#     numero1 = input("Introduzca un número: ")
#     numero1 = int(numero1) 

# except:
#     print("Error. Debes introducir un número.", file=sys.stderr)  # El segundo argumento indica la salida
#     sys.exit()

# # Lo mismo para numero2, aunque es más recomendable indicar qué tipo de excepción queremos capturar:
# try:
#     numero2 = input("Introduzca un número: ")
#     numero2 = int(numero2) 

# except ValueError as e:
#     print("Error. Debes introducir un número.", file=sys.stderr)  # El segundo argumento indica la salida
#     sys.exit()

# La forma correcta para escribir esto es:

numero1 = input("Introduzca un número: ")
numero2 = input("Introduzca un número: ")

try:
    numero1 = int(numero1)
    numero2 = int(numero2)

except ValueError:
    print("Error. Debes introducir un número.", file=sys.stderr)  # El segundo argumento indica la salida
    sys.exit()

resultado = numero1 < numero2

if resultado:
    print(numero1, " es menor que ", numero2)

else:
    print(numero1, " es mayor que ", numero2)

# Bloques iterativos:

# numero = input("Introduzca un número entre 1 y 10: ")

# try:
#     numero = int(numero)
# except:
#     numero = 0

# while not 1 <= numero <= 10:

#     # Volver a pedir introducir número:
#     numero = input("Introduzca un número entre 1 y 10: ")

#     try:
#         numero = int(numero)
#     except:
#         numero = 0

# print("Mu bien, te sabes los números")

# Como hay que repetir código, existe una mejor opción:

while True:
    numero = input("Introduzca un número entre 1 y 10: ")

    try:
        numero = int(numero)
    except:
        pass # Como es un bucle infinito, no hay que poner el valor a 0

    if 1 <= numero <= 10:
        break

print("Mu bien, te sabes lo números")

