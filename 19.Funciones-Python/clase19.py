# "funciones(def)" Sirven para guardar porciones de lógica(BLOQUES DE CODIGO REUTILIZABLES) que tienen una tarea en especifico
# last_name="No tiene apellido" VIENE A SER un "parámetros con valor por defecto o parámetros predeterminados"
def greet(name, last_name="No tiene apellido"):
    print("Saludo -> Hola" , name, last_name)

greet("Rogger", "Meneses")
greet("Roosevelt")
# argumentos nombrados (keyword arguments)
# Van directamente de acuerdo a su parametro no importa su orden
greet(last_name="Meneses", name="Rogger")





