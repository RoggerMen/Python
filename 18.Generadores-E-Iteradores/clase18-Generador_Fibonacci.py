# Fibonacci ES:
# el resultado de 0 + 1 es 1, el resultado de 1 + 2 es 3 y asi sucesivamente con cada numero que salga( ES OBTENER UN VALOR SUMANDO LOS 2 ANTERIORES)
# 0 1 1 2 3 5 8 13 21....

def fibonacci(limit):
    '''
    "a, b = 0, 1" ES IGUAL COMO SI ESTUVIERAMOS HACIENDO:
    a = 0
    b = 1
    '''
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a+b

for num in fibonacci(21):
    print(num)



