import csv

# Leer archivo
'''with open('31.Manejo-Archivos-CSV/products.csv', mode='r') as file:
    # ESTE VA A SER EL OBJETO DONDE VA A ESTAR TODA LA INFORMACION
    # LE DECIMOS A "csv" QUE QUEREMOS A ABRIR ESTA INFORMACIÓN EN UN FORMATO DE DICCIONARIO(DictReader)(ES LO QUE SE ESTAN RELACIONADOS POR UNA LLAVE CON SU VALOR "llave:valor"(key:value))
    csv_reader = csv.DictReader(file)
    # Por cada fila que nosotros vamos a estar iterando LA VAMOS A VISUALIZAR
    for row in csv_reader:
        print(row)'''

# Mostrar la información por columnas
with open('31.Manejo-Archivos-CSV/products.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(f"Producto: {row['name']}, Precio: {row['price']}")



