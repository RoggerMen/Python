# Generador de numeros impares
def num_impar (limit):
    a=1
    while a < limit+1:
        yield a
        a= a+2
for num in num_impar (11):
    print (num)
print("-------------------------")
# Generador de numeros pares
def num_pares(limit):
    a=0
    while a < limit+1:
        yield a
        a=a+2
for num in num_pares (10):
    print (num)