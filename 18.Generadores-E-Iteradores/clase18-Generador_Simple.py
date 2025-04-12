
# USAMOS EL "yield"
# SIRVE para DEVOLVER VALORES, NO SOLO PERMITE UN VALOR SINO VARIOS VALORES, retornamos/devolvemos VARIOS VALORES
def my_generator():
    yield 1
    yield 2
    yield 3

for value in my_generator():
    print(value)



