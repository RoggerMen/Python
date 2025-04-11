# LISTA DE LISTAS a estos se les conoce como "MATRICES"
# LAS MATRICES TIENEN LAS MISMAS PROPIEDADES QUE LAS LISTAS, TAMBIEN PODEMOS AÑADIR INFO, ELIMINAR O INCLUSO MODIFICARLAS (ES DECIR: DATOS MUTABLES)
# CREAMOS LA MATRIZ
matrix =[[1,2,3],
         [4,5,6],
         [7,8,9]]
print(matrix)
#TENEMOS ACCESO A NUESTRA PRIMERA LISTA( QUE VIENE A SER UN ELEMENTO)
# AL PODER HACER ESTO COMO EJEMPLO SEA AÑADIR O MODIFICAR O ELIMINAR SE LES LLAMA "DATOS MUTABLES"
# COSA QUE CON LA TUPLA QUE MAS ADELANTE SE VE NO PASA(DATOS INMUTABLES)
print(matrix[0])
matrix[0] = "uno"
print(matrix[0])
print(matrix)
print(matrix[2][1])


# AÑADIMOS UNA DIMENSION MAS A NUESTRO EJEMPLO Y VAMOS A ITERAR ATRAVES DE ESTOS ELEMENTOS
matrix_2 = [[[1,2],
            [3,4]],
            
            [[5,6],
            [7,8]]]
print(matrix_2)
#Si queremos Mostrar el ELEMENTO 6
print(matrix_2[1][0][1])

# TUPLAS -> una tupla es una colección ordenada de elementos(INMUTABLES)
# TUPLAS EN PYTHON -> CLASES INMUTABLES(DATOS INMUTABLES) -(una vez creada, no puedes modificar sus valores (ni añadir, ni eliminar elementos).
# podemos colocar si queremos las parentesis o tambien puede ir sin parentesis "()" PARA SABER QUE SON TUPLAS
# PYTHON lo sobreentiende 
# eje. numbers = 1,2,3,4,5 
# PYTHON entiende que es una "class tuple"(TUPLA - FILA)
numbers = (1,2,3,4,5)
print(numbers)
print(type(numbers))
print(numbers[0])

numbers[0] = 'uno'
# NOS DARÁ ERROR PORQUE LA TUPLA ES "INMUTABLE" Y AQUI ESTAMOS MODIFICANDO COSA QUE NO SE PUEDE HACER A UNA TUPLA
print(numbers)
