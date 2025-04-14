def dividir():
    divisor = int(input("Ingresa un número divisor: "))
    result = 100 / divisor
    return print(result)
# USAMOS EL "try-except" PARA DAR UN MENSAJE

try: # EL "pass" HACE PASAR EL BLOQUE "try"
    dividir()
except ZeroDivisionError as e:
    print("Error: El divisor no puede ser CER")
    print("Ha ocurrido el error de TIPO", e)
except ValueError as e:
    print("Ha ocurrido el error de TIPO", e)
    print("Error: No colocar letras, SOLO NÚMEROS\n" + "INTENTELO NUEVAMENTE")
    dividir()

# CAPTURAR UNA "excepcion" EN UNA VARIABLE PARA OBTENER MAS INFORMACION



# De la Forma con un "bucle" "while" YA QUE EL ANTERIOR SE ROMPE(MI MANERA)

# De la Forma con un "bucle" "while" YA QUE EL ANTERIOR SE ROMPE(MI MANERA)
'''def dividir():
    while True:
        try:
            divisor = int(input("Ingresa un número divisor: "))
            result = 100 / divisor
            print(result)
            break  # Salir del bucle si todo salió bien
        except ValueError as e:
            print("❌ Error: No colocar letras, SOLO NÚMEROS")
        except ZeroDivisionError as e:
            print("❌ Error: El divisor no puede ser CERO")

dividir()'''


