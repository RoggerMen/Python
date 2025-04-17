import json

file_path = '32.Manejo-Archivos-JSON/products.json'

new_product = {
    "name": "Wireless Charger",
    "price": 75,
    "quantity": 100,
    "brand": "ChargeMaster",
    "category": "Accessories",
    "entry_date": "2024-07-01"
}
# PARA LEER LA INFORMACION
with open(file_path, mode='r') as file:
    products = json.load(file)

products.append(new_product)

# PARA ESCRIBIR LA INFORMACION
with open(file_path, mode='w') as file:
    # AL metodo "dump()" se le pasa 3 PARAMETROS, Convierte automáticamente objetos de Python en texto JSON, convierte un objeto de Python (como listas, diccionarios, etc.) en un archivo JSON legible
    # "products" ES LA INFORMACION QUE NOSOTROS QUEREMOS ESCRIBIR EN EL ARCHIVO
    # "file" ES EL ARCHIVO
    # "indent" ES LA IDENTACION PARA OBTENER UN ORDEN( CON FINES DE BUENA ESTRUCTURA Y MEJOR LEGIBILIDAD)
    json.dump(products, file, indent=4)
    
    
    