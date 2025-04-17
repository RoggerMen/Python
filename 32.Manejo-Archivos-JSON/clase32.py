# importar libreria JSON
import json

# LECTURA DEL ARCHIVO
with open('32.Manejo-Archivos-JSON/products.json', mode='r') as file:
    # CARGAMOS LA INFORMACION DEL ARCHIVO
    products = json.load(file)

# Mostrar el contenido
for product in products:
    #print(product)
    # EXTRAEMOS EL PRODUCTOS por medio de sus LLAVES
    print(f"Product: {product['name']}, Price: {product['price']}")





