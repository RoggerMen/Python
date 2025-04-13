# Funciones anonimas(Sin Nombre) o lambda
# Solo necesita parametros y una operación para aplicar a ella
'''
Una **función lambda** en Python es una función anónima, es decir, una función que no tiene nombre y se define en una sola línea usando la palabra clave lambda. Estas funciones son útiles para operaciones simples y cortas que se pueden definir rápidamente sin la necesidad de una función formal.

#### Sintaxis de una Función Lambda



lambda argumentos: expresión
- **argumentos**: Son los parámetros que la función tomará.

- **expresión**: Es una única expresión que se evalúa y devuelve como resultado de la función.
'''
add = lambda a, b: a + b
print(add(10,4))

multiply = lambda a, b: a* b
print(multiply(80, 5))

# CUANDO TRABAJAMOS CON "listas" y queremos aplicar una FUNCION a cada uno de estos elementos PODEMOS UTILIZAR "map()" ACOMPAÑADO DE "lambda"
# Elevado al Cuadrado de cada número del 1 al 10
numbers = range(11)
print( numbers)
squared_numbers = list(map(lambda x: x**2, numbers))
print("Elevados al Cuadrado:", squared_numbers)


# Tambien hay una manera de seleccionar los elementos si cumplen una condición, para eso vamos a utilizar la función "filter()"

# Pares
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Pares:", even_numbers)
