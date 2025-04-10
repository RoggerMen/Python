to_do = ["Dirigirnos al hotel",
         "Ir a almorzar",
         "Visitar un museo",
         "Volver al hotel"]
print(to_do)

numbers = [1, 2, 3, 4, "cinco"]
print(numbers)
# Python reconoce este tipo de datos con "class list"
print(type(numbers))

mix = ["uno", 2, 3.14, True, [1, 2, 3]]
print(mix)

# Consultamos cuantos datos tenemos guardados o almacenados O PREGUNTAR CUANTOS ELEMENTOS TIENE
print(len(mix))

# OTRA PROPIEDAD ES LA DE "indexación"(POR SU INDICE)
print("Primer Elemento: ", mix[0])
print("Segundo Elemento: ", mix[1])
print("Último elemento: ", mix[-1])

# slice
string = "Hola mundo"
print("Primer Elemento: ", string[0])
print("Segundo Elemento: ", string[1])
print("Último elemento: ", string[-1])
# Si tomamos en cuenta el final, le restamos 1 posicion osea que no saldria desde la "posición 0"(Primera posición) hasta la "posición 2" sino hasta la posición 1(OSEA DARIA LA POSICION 0 Y 1, NO VA HASTA LA POSICION 2)
print(mix[0:2])

# ESTO VENDRIA A SER IGUAL AL DE ARRIBA SOLO QUE NO ESPECIFICAMOS EL INICIO,Y DE ESTA MANERA SERIA UNA MEJOR PRACTICA
print(mix[:2])

# TAMBIEN LO MISMO CON EL FINAL, seria desde la "posición 2" HASTA EL FINAL
print(mix[2:])

# EN CAMBIO si nosotros lo colocamos DANDOLE UN INICIO(DE DONDE EMPIEZA) Y EL FINAL CON UN -1 o -2 ...etc, ESTE NO TOMARÁ EL FINAL SI NO UNO ANTES QUE ESTE(EL FINAL) 
print(mix[2:-1])

# METODOS DE LISTAS
# "append()"Si queremos "aumentar" o "añadir" un nuevo valor/ELEMENTO al final de nuestra lista
mix.append(False)
print(mix)

mix.append(["a","b"])
print(mix)

# "insert()" SI QUEREMOS INSERTAR UN DATO/ELEMENTO DICIENDOLE LA POSICION QUE QUERRAMOS,
# POR EJEMPLO AQUI LE DAMOS LA POSICION EN LA QUEREMOS INSERTAR EL DATO/ELEMENTO Y LUEGO IMPRIMIMOS PARA COMPROBAR
mix.insert(1,["a","b"])
print(mix)

# CON EL "index()" HACEMOS USO DE INDEXACION Y PREGUNTAMOS EN QUE POSICIÓN SE ENCUENTRA DICHO DATO
# SI DICHO DATO/ELEMENTO SE REPITE COMO EN ESTA OCASION: ['uno', ['a', 'b'], 2, 3.14, True, [1, 2, 3], False, ['a', 'b']]
# VA A TOMAR EL INDICE(POSICION) DEL PRIMER DATO(LA PRIMERA APARICION DEL DATO), EN ESTE CASO SERIA "posición 1"
print(mix.index(["a","b"]))

# CON "max()"(TE DA EL MAYOR DATO/ELEMENTO) CON "min()(TE DA EL MENOR DATO/ELEMENTO)"
# CUANDO TRABAJAMOS CON LISTA DE NUMEROS QUE PUEDEN SER FLOTANTES O ENTEROS, PODEMOS CONSULTAR CUAL ES ELEMENTO MAYOR Y CUAL EL MENOR
numbers = [1, 2, 100.01, 90.45, 3, 4, 5]
print(numbers)
print("Mayor:", max(numbers), "\nMenor:", min(numbers))

# "del" ELIMINAR ELEMENTOS DE LA LISTA
del numbers[-1]
print(numbers)

# Eliminamos una porción de Datos, DE LA POSICION 0 HASTA LA POSICION 1, ya que RECUERDA que NO AGARRA A LA "POSICION 2" SINO HASTA LA "POSICION 1"
del numbers[:2]
print(numbers)

del numbers
# NOS DA UN ERROR DE TIPO "NameError", NameError: name 'numbers' is not defined. Did you forget to import 'numbers'?
# ESTO ES PORQUE AQUI YA ELIMINAMOS A LA LISTA "numbers" Y NO TIENE QUE IMPRIMIR ENTONCES POR ESO NOS DA EL ERROR
print(numbers)

