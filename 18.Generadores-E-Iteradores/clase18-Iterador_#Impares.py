# Crear un iterador para los numeros impares

# Limite

limit = 10
print("\nPARES: ")
# si son pares EMPEZAMOS CON "0"
odd_iter = iter(range(0,limit+1, 2))
# Usar el iterador
for num in odd_iter:
    print(num)

print("\nIMPARES: ")
# Crear el iterador, SI SON IMPARES EMPEZAMOS CON 1
odd_iter = iter(range(1,limit+1, 2))

# Usar el iterador
for num in odd_iter:
    print(num)

