# CON COMILLAS DOBLES("")
name = "ROGGER Roosevelt"
caracter = "R"
# CON COMILLAS SIMPLES ('')
name2 = 'Rogger Roosevelt'
# CON 3 COMILLAS SIMPLES (''' ''')
# ESTO PERMITE DAR SALTOS EN LINEA CON ENTER LOS ANTERIORES NOS DAN ERRORES SI LE DAMOS ENTER
name3 = '''Rogger 


Roosevelt'''
print(type(name))
print(type(caracter))
print(type(name2))
print(type(name3))

print(name)
print(name2)
print(name3)

#INDEXACION PODEMOS FIJAR DE ACUERDO A LA POSICION DE CADA LETRA DE LA CADENA(0,1,2,3,4,...)
# LA PRIMERA POSICION ES EL [0]
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])

# SI QUEREMOS LA PARTE FINAL LA HACEMOS CON EL "-1"
print(name[-1]) 
# Y ASI DE LA PARTE FINAL SI QUEREMOS LA SEGUNDA LETRA DE LA PARTE FINAL LE COLOCAMOS EL -2
print(name[-2])

# CONCATENACION -> SUMAMOS CADENAS
last_name = "  Meneses  "
print(name + " " +  last_name)

# REPETICION -> QUEREMOS MULTIPLICAR O REPETIR CIERTAS VECES LA CADENA QUE QUEREMOS
print(name * 5)

# CONSULTA LONGITUD (len) -> CUANTOS CARACTERES TIENE LA VARIABLE
print(len(name))
print(len(last_name))

# METODOS DEL TIPO "STRING" ->  lower( PARA PONER TODO EN MINUSCULA), upper( PARA PONER TODO EN MAYUSCULA),strip( PARA ELIMINAR LOS ESPACIOS)
print(name.lower())
print(name.upper())
print(last_name.strip())