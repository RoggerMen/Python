# LEER UN ARCHIVO LINEA POR LINEA

# LA INFORMACION QUE LE ENVIAMOS AL "open()-abrir" ES EL NOMBRE DE LA CARPETA Y BUSCAR AL ARCHIVO Y SI ESTA EN LA MISMA RUTA SOLAMENTE COLOCAR EL NOMBRE DEL ARCHIVO
# "r" ES POR EL "read" (leer)
# CON EL "as file" LE DECIMOS QUE LO QUEREMOS ABRIR COMO UN ARCHIVO(file es el nombre que nosotros le estamos poniendo a lo que estamos extrayendo de "cuento.txt")
'''with open('30.Manejo-Archivos-TXT/cuento.txt', 'r', encoding='utf-8') as file:
    # Le decimos que por cada una de las lineas, el archivo "file"
    for lineas in file:
        # NOSOTROS VAMOS A DECIRLE que queremos "lineas", el "strip()" lo que hace es eliminar los "espacios" y "saltos de linea" que tenemos al final
        print(lineas.strip()) '''
        

# AÑADIR TODAS LA LINEAS EN UNA LISTA
# EL METODO "readlines()" LEER TODAS LAS LINEAS DEL "TEXTO"(,txt) PARA GUARDAR O ALMACENAR en una "lista"

'''with open('30.Manejo-Archivos-TXT/cuento.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    print(lines)'''


# AÑADIR TEXTO
# ya no colocamos como referencia a 'r'(read) ahora es la referencia 'a'(append - añadir)
# LO QUE HACE ES AÑADIR MAS TEXTO AL ARCHIVO CON EL REFERENCIADO "a" y al hacer el "file.write"

'''with open('30.Manejo-Archivos-TXT/cuento.txt', 'a') as file:
    file.write("\n\nBY:Rogger")'''



# SOBREESCRIBIR EL TEXTO
# SOBREESCRIBIRLOS eliminar la información que ya esta, ESTO LO HACEMOS CON 'W'(write-escribir) 
# ESTO PUEDE CAUSARTE PROBLEMAS, YA QUE BORRARIA TODOS TUS DATOS Y SOBREESCRIBIRIA LO QUE LE ESCRIBAS AL ARCHIVO
'''with open('30.Manejo-Archivos-TXT/cuento.txt', 'w') as file:
    file.write("\n\nBY:Rogger")'''

# PRIMERA FORMA DE ¿CUANTOS LINEAS TIENE EL CUENTO?
with open ("30.Manejo-Archivos-TXT/cuento.txt", "r") as archivo:

    lineas = archivo.readlines()

    print(len(lineas))

# SEGUNDA FORMA
file = open('30.Manejo-Archivos-TXT/cuento.txt', 'r')
lines = file.readlines()
n_lines = 0

for line in lines:
    n_lines += 1
print(f"el cuento del archivo tiene {n_lines} lineas")
file.close()
