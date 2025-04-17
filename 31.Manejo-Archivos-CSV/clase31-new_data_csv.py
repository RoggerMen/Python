import csv

new_product = {
    'name': 'Wireless Charger',
    'price': 75,
    'quantity': 100,
    'brand': 'ChargerMaster',
    'category': 'Accessories',
    'entry_date': '2025-07-01'
}
# "newline=''" Es la forma de lectura, la cual es sin ningun caracter y ningun espacio
with open('31.Manejo-Archivos-CSV/products.csv', mode='a', newline='') as file:
    file.write('\n')
    csv_writer = csv. DictWriter(file, fieldnames = new_product.keys())
    csv_writer.writerow(new_product)


