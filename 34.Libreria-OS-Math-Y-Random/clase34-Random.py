
import random

# GENERAR UN NUMERO ENTERO ALEATORIO
random_number = random.randint(1,10)
print(random_number)


# ELEGIR COLORES ALEATORIOS
colors = ['Rojo', 'Azul', 'Verde']
random_color = random.choice(colors)
print(random_color)

# BARAJAR UNA LISTA DE CARTAS
cards = ['As', 'King', 'Queen', 'Jot', '10']
random.shuffle(cards)

print(cards)
