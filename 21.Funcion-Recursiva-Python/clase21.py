# La "RECURSIVIDAD" es una técnica de la programación, donde UN PROGRAMA SE LLAMA ASI MISMO PARA PDOER RESOLVER UN PROBLEMA.

# Hallar el Factorial de un Número
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

factorial_5 = print(factorial(10))


# "RECURSIVIDAD" en fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

number = 7
print(fibonacci(number))


