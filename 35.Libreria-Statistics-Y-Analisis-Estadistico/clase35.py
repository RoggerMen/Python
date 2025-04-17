import statistics

import csv


# Leer los datos de ventas mensuales desde un archivo CSV
monthly_sales = {}
with open('35.Libreria-Statistics-Y-Analisis-Estadistico/monthly_sales.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        month = row['month']
        sales = int(row['sales'])
        monthly_sales[month] = sales

sales = list(monthly_sales.values())
print(sales)


# LA "MEDIA", es la suma de todos los datos dividido entre el número TOTAL
# Hallar la media
mean_sales = statistics.mean(sales)
print("La media es: ", mean_sales)


# Hallar la mediana
median_sales = statistics.median(sales)
print("La mediana es: ", median_sales)


# Hallar la moda
mode_sales = statistics.mode(sales)
print("La moda es: ", mode_sales)


# Hallar la Desviación Estándar
stdev_sales = statistics.stdev(sales)
print("La Desviación Estándar es: ", stdev_sales)



# Hallar la varianza
variance_sales = statistics.variance(sales)
print("La Varianza es: ", variance_sales)


# MAXIMO Y MINIMO - Ventas más altas y más bajas
max_sales = max(sales)
min_sales = min(sales)
print(max_sales ,"Y",min_sales )


# RANGO DE VENTAS - Diferencia entre la venta más alta y la más baja
range_sales = max_sales - min_sales
print(f"Rango de Ventas: {range_sales}")

