# Piensa en las "Comprehesion Lists" COMO el expreso de PYTHON -> SON BREVES RAPIDAS Y POTENTES
# CON ELLAS puedes CONSTRUIR LISTAS de manera concisa, expresiva y eficiente
squares = [x**2 for x in range(1,11)]
print("Cuadrados: ", squares)

celsius = [x*10 for x in range(0,5)]
print(celsius)
fahrenheit = [(temp * 9/5) + 32 for temp in celsius]
print("Temperatura en °F: ", fahrenheit)

# Numero pares
''' ******** LEEMOS ASI: **********
DESDE EL "for" leemos : POR CADA VALOR DE "X" QUE ESTA EN EL RANGO DE 0 AL 20(NO TOMA EL ULTIMO VALOR(21)) POR CADA UNO DE ESTOS NUMEROS, SI "X" MODULO 2 ES IGUAL A 0 OSEA ES "PAR" O TAMBIEN "pero solo incluye los que sean DIVISIBLES entre 2" ENTONCES SE VA A AÑADIR A LA LISTA
Y DE ESTA MANERA NOS DA TODOS LOS NUMEROS PARES
'''
evens = [x for x in range(21) if x % 2==0]
print(evens)

# ESTRUCTURAS UN POCO MAS COMPLEJAS - MATRICES
# HALLAMOS LA TRANSPUESTA DE UNA MATRIZ, ES UNA OPERACION QUE CONSISTE EN INTERCAMBIAR SUS FILAS POR COLUMNAS
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
# CREAMOS LA TRANSPUESTA
# COMO ESTAMOS TRABAJANDO EN UNA MATRIZ VAMOS ATAMBIEN OBTENER UNA MATRIZ PERO MODIFICADA
''' ********* LEEMOS ************
Desde el for decimos, POR(for) cada una de estas FILAS(row) EN(in) la MATRIX(matrix) YO OBTENGA EL DATO QUE ESTA EN LA FILA (row[i])
* El ITERADOR "i" viene del "for" "i" -> AQUI LO CREAMOS
* Que va a estar EN(in) un RANGO(range)
* PREGUNTAMOS Cual es la dimension de la lista que vamos a tener de "matrix" OSEA VIENE A SER "len(matrix[0]) y le DAMOS como DATO INICIAL "0" Y ESTE ES EL VALOR QUE IRA AHI
MUESTRA MENOS CODIGO
'''
transposed =[[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transposed)

#MUESTRA MAS CODIGO
print("SIN EL COMPREHENSION LIST")
#creamos una lista vacia
transposed = []
for i in range(len(matrix[0])):
    print(i)
    transposed_row = []
    for row in matrix:
        print(transposed_row)
        transposed_row.append(row[i])
    transposed.append(transposed_row)
    print(transposed_row)

print(transposed)

