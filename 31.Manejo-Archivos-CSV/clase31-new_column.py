
import csv

file_path = '31.Manejo-Archivos-CSV/products.csv'
updated_file_path = '31.Manejo-Archivos-CSV/products_updated.csv'

with open(file_path, mode='r') as file:
    csv_reader = csv.DictReader(file)
    #Obtener los nombres de las columnas existentes Y AUMENTAMOS un campo mas "total_value"
    fieldnames = csv_reader.fieldnames + ['total_value']

# EMPEZAMOS A ESCRIBIR EL NUEVO ARCHIVO
    with open(updated_file_path, mode='w', newline='') as updated_file:
        csv_writer = csv.DictWriter(updated_file, fieldnames=fieldnames)
        csv_writer.writeheader() #Escribir los encabezados

        for row in csv_reader:
            row['total_value'] = float(row['price']) * int(row['quantity'])
            csv_writer.writerow(row)


