# ----------------------------------------------------------------------------
# PYTHON 3 - APUNTES Y EJEMPLOS
# Ejemplos básicos
# ----------------------------------------------------------------------------
# Autor: Juan Ocaña Valenzuela
# GitHub: patchispatch
# Este documento está regulado por la licencia GNU General Public License v3.0
# ----------------------------------------------------------------------------

# En esta parte veremos cómo mostrar y pedir datos por pantalla, 
# y también los diferentes tipos. También comprenderemos cómo utilizar
# las variables en Python, los operadores de comparación, los diferentes tipos
# de bloques, y echaremos un breve vistazo al manejo de excepciones con el 
# bloque try.

# ----------------------------------------------------------------------------
# Entradas y salidas por pantalla.

# Comencemos por lo básico: un "Hola, mundo":
print ("¡Hola, mundo!")

# La función print() nos permite enviar una cadena de caracteres a la salida
# estándar. Podemos dar forma a la salida de varias formas, pero eso lo veremos
# un poco más adelante.

# De momento, vamos a ver cómo pedir datos por la entrada estándar:
informacion = input("Introduzca lo que sea: ")

# La función input() permite solicitar un valor al usuario, y lo devolverá.
# En este caso, se asigna a la variable informacion, que acabamos de declarar. 
# Pero, ¿de qué tipo es esta variable? 

# En Python, el tipo de las variables es dinámico, es decir, se asigna en 
# tiempo de ejecución. Por tanto, informacion puede contener un dato de 
# cualquier tipo (aunque podremos comprobar cuál es). No necesitamos declarar
# las variables con un tipo.

# Ahora que tenemos la información que nos ha dado el usuario, vamos a 
# imprimirla por pantalla. La función print() permite varias sintaxis para
# realizar esto, aunque de momento vamos a fijarnos en esta:
print("Ha introducido: ", informacion, ".")

# ----------------------------------------------------------------------------
# Comparaciones:

# En Python, los operadores de comparación son incluso más sencillos de usar
# que en otros lenguajes, aunque su comportamiento es el mismo. Pero para 
# hablar de comparaciones, debemos hablar de valores booleanos.

# Una variable booleana puede ser cierta (True) o falsa (False). Al realizar 
# una comparación, se devuelve uno de estos valores. 

# IMPORTANTE: Python distingue entre mayúsculas; True y False deben escribirse
# así.

# En este ejemplo, pediremos dos números al usuario, y devolveremos si el 
# primero es menor que el segundo:

numero1 = input("Introduzca un número: ")
numero2 = input("Introduzca otro número: ")

resultado = numero1 < numero2

print (numero1, "<", numero2, ": ", resultado)

# Esto debería funcionar bien. Sin embargo... no lo hace. Esto se debe a que 
# al leer desde la entrada estándar (el teclado), se guardan cadenas de 
# caracteres, no números. Para que pueda compararlos como tal, debemos realizar
# la conversión del tipo, en este caso, a números enteros:

# Una forma de hacerlo:
numero1 = input("Introduzca un número: ")
numero1 = int(numero1) 

# Otra forma de hacerlo; más corta, pero menos legible y más difícil de 
# depurar:
numero2 = int(input("Introduzca otro número: "))

# Ahora, nuestra comparación funciona sin problema, siempre y cuando se 
# introduzcan dos números. En caso contrario, nuestro programa mostrará un 
# precioso error: se trata de una excepción. Si algo no va bien, se generará
# una excepción, y si nadie se encarga de capturarla y responder a ella, el
# programa no se hará responsable de lo que pueda ocurrir, y probablemente se 
# detenga. Pero podemos hacer algo, y para ello, debemos importar el 
# módulo sys. 
import sys

# Ahora disponemos de una variable sys, que apunta al módulo. Si te preguntas 
# por qué, se explicará más adelante. De momento, nos basta con saber que
# este módulo contiene un método exit(), que nos permitirá salir del programa
# al llamarlo.

# Nuestra intención es:
# Si el usuario introduce un número, continuar.
# Si se produce una excepción, escribir un mensaje y salir.

# Llamaremos a la sección del código en la que se puede producir una excepción,
# sección crítica. En nuestro aso, es la conversión de tipo a entero.
# Para capturar las posibles excepciones, debemos escribirla en un bloque 
# llamado try;
try:
    numero1 = input("Introduzca un número: ")
    numero1 = int(numero1) 

# Y ahora, en caso de producirse una excepción, se ejecutará aquello que 
# especifiquemos en el bloque except:
except:
    # Modificando file cambiamos la salida. En este caso, usamos la de error.
    print("Error. Debes introducir un número.", file=sys.stderr)  
    sys.exit()

# Hacemos lo mismo para numero2, aunque es más recomendable indicar qué 
# tipo de excepción queremos capturar. En este caso es del tipo ValueError:
try:
    numero2 = input("Introduzca un número: ")
    numero2 = int(numero2) 

except ValueError:
    print("Error. Debes introducir un número.", file=sys.stderr)
    sys.exit()

# Estamos repitiendo código, así que una forma mejor de escribir esto sería:

numero1 = input("Introduzca un número: ")
numero2 = input("Introduzca un número: ")

try:
    numero1 = int(numero1)
    numero2 = int(numero2)

except ValueError:
    print("Error. Debes introducir un número.", file=sys.stderr)
    sys.exit()

resultado = numero1 < numero2

if resultado:
    print(numero1, " es menor que ", numero2)

else:
    print(numero1, " es mayor que ", numero2)

# Con estas herramientas podremos realizar comparaciones y muchas más cosas,
# evitando errores por el camino.

# ----------------------------------------------------------------------------
# Bloques iterativos:

# Nuestro siguiente paso es conocer cómo funcionan los bloques iterativos.
# Empezaremos por el bloque while.

# En este ejemplo, queremos pedir al usuario un número entre el 1 y el 10, 
# y hasta que no introduzca un número válido, se seguirá solicitando.
# Podemos realizarlo con un bucle while:

numero = input("Introduzca un número entre 1 y 10: ")

try:
    numero = int(numero)
except:
    numero = 0

while not 1 <= numero <= 10:

    # Volver a pedir introducir número:
    numero = input("Introduzca un número entre 1 y 10: ")

    try:
        numero = int(numero)
    except:
        numero = 0

print("Muy bien, te sabes los números.")

# El funcionamiento de while es muy sencillo: mientras se cumpla la condición
# indicada, el bloque se repite. En este caso, si el usuario no introduce un
# número válido, se repetirá.

# Existe una mejor forma para expresarlo, ya que estamos repitiendo código:

while True:
    numero = input("Introduzca un número entre 1 y 10: ")

    try:
        numero = int(numero)
    except:
        pass # Como es un bucle infinito, no hay que poner el valor a 0

    if 1 <= numero <= 10:
        break

print("Muy bien, te sabes lo números.")

# while True es un bucle infinito, ya que la condición siempre es cierta.
# Para salir de él, se utiliza la palabra reservada break.

# Inicializacion de arrays:
array = [1, "ola k ase", false]

# foreach de Python, donde imprimirá los valores del array.
for val in array:
    print(val)

# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------

