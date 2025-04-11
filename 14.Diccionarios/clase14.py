# LOS DICCIONARIOS son una estructura que ALMACENAN 2 datos "clave:valor" SON "MUTABLES"
numbers = { 1: "uno",
            2: "dos",
            3: "tres"}

print(numbers)

# CONSULTAMOS SEGUN SU CLAVE/LLAVE PARA OBTENER SU VALOR
print(numbers[2])

information = { "nombre": "Rogger",
                "Apellido": "Meneses",
                "Altura": 1.72,
                "Edad": 23}

print(information)
del information["Edad"]
print(information)
# METODO "keys() CON LA CUAL PEDIMOS cuales son las CLAVES/LLAVES POR SI TENEMOS DUDAS
claves = information.keys()
print(claves)
print(type(claves))

# METODO "values()" PARA PEDIR LOS VALORES
values = information.values()
print(values)

# METODO "items()" PARA TRAER A LOS PARES DE VALOR(key:value(clave/llave y valor))

pairs = information.items()
print(pairs)

contacts = {"Rogger":{
            "Apellido": "Meneses",
            "Altura": 1.72,
            "Edad": 23},
            "Mia":{
            "Apellido": "Meneses",
            "Altura": 1.65,
            "Edad": 21}}
print(contacts)
print(contacts["Rogger"])
