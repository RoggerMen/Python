def add( a, b):
    return a + b

def substract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        print("Error: No se puede dividir por 0")
    else:
        return a / b


def calculator():
    while True:
        print("Seleccione una operación: ")
        print("1.Suma")
        print("2.Resta")
        print("3.Multiplicación")
        print("4.División")
        print("5.Salir")

        option = input("Ingrese su opción (1,2,3,4,5): ")
        
        if option == "5":
            print("Saliendo de la calculadora")
            break
        
        if option in ["1","2","3","4"]:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            
            if option == "1":
                print(" La suma es:", add(num1, num2),"\n")
            elif option == "2":
                print("La resta es:", substract(num1, num2),"\n")
            
            elif option == "3":
                print("La multiplicación es:", multiply(num1, num2),"\n")
            elif option == "4":
                print("La multiplicación es:", divide(num1, num2),"\n")
        else:
            print("Opción no válida, Por favor intenta de nuevo\n")

calculator()


# TAMBIEN PODEMOS USAR UN "match - case" ES TIPO UN "switch - case"
'''
match es una estructura de control introducida en la versión 3.10, usada para realizar una especie de "comparación inteligente" de valores

La estructura de match te permite comparar un valor contra varios patrones y ejecutar código basado en el patrón que coincida.

def analizar_datos(datos):
    match datos:
        case (x, y) if x > y:
            return "La primera parte es mayor."
        case {"nombre": nombre, "edad": edad}:
            return f"El nombre es {nombre} y tiene {edad} años."
        case _:
            return "Patrón no reconocido."

# Llamadas:
print(analizar_datos((5, 3)))  # Resultado: La primera parte es mayor.
print(analizar_datos({"nombre": "Ana", "edad": 30}))  # Resultado: El nombre es Ana y tiene 30 años.

'''