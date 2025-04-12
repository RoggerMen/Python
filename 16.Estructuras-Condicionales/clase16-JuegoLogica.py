# DE MANERA MAS USANDO CONDICIONALES
print( 'BIENVENIDO AL JUEGO PIEDRA, PAPEL O TIJERA')
print( 'JUGADOR 1 INGRESA TU NOMBRE: ')
player_1_name = input()

print( 'JUGADOR 2 INGRESA TU NOMBRE: ')
player_2_name = input()

print("player_1_name,ingresa qué eliges: ¿piedra, papel o tijera?: ")

player_1_move = input( ). lower()

print("player_2_name,ingresa qué eliges: ¿piedra, papel o tijera?: ")

player_2_move = input(). lower()

valid_moves = ['piedra', 'papel', 'tijera']

if player_1_move not in valid_moves or player_2_move not in valid_moves:
    print("Uno o ambos jugadores hicieron una elección no válida. Por favor, elijan entre piedra, papel o tijera.")
else:
    if player_1_move == player_2_move:
        print ('Empate')
    elif(player_1_move == 'piedra' and player_2_move == 'tijera') or (player_1_move == 'tijera' and player_2_move == 'papel') or (player_1_move == 'papel' and player_2_move == 'piedra'):
        print( 'Gana: ', player_1_name)
    else:
        print( 'Gana: ', player_2_name)



''' LOGICA DE JUEGO PIEDRA PAPEL O TIJERA(DICCIONARIO)

utilice un diccionario que tiene la llave y valor que le gana a que ejemplo la piedra le grana a la tijera (piedra : tijera) 
y posterior a esto solo se pide ingresar la opcion al jugador 
y colocar las debidas condicionales con la busqueda en el diccionario: opciones.get(jugador1) 
y se compara con la opción del otro jugador

'''

opciones = { "piedra": "tijera", 
            "papel": "piedra", 
            "tijera": "papel"}

print("JUEGUEMOS AL 'piedra','papel' o 'tijera'")

jugador_1 = input("Jugador 1, elija piedra, papel o tijera:\n ").lower()
jugador_2 = input("Jugador 2, elige piedra, papel o tijera:\n ").lower()

if jugador_1 == jugador_2:
    print("Empate")
elif opciones.get(jugador_1) == jugador_2:
    print("Gana jugador 1")
elif opciones.get(jugador_2) == jugador_1:
    print("Gana jugador 2")
else:
    print("Opción no válida")
