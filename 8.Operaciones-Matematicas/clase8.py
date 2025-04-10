# Operadores Numéricos
a = 10
b = 3

print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
# POTENCIACIÓN
print("Potenciación:", a ** b)
# NO SE PUEDE HACER DIVISIONES ENTRE "0"
print("División:", a / b)
# DOBLE DIVISION(PARTE ENTERA DE LA DIVISION)
print("Parte entera de la División:", a // b)

# viene a ser el residuo/resto(Lo que sobra de una división) de dicha división
print("Módulo:", a % b)

# SHORTCUTS(ATAJOS)
z = 10
# "z += 2" VIENE A SER IGUAL A "z = z + 2"
z += 2
print(z)
# "z += 2" VIENE A SER IGUAL A "z = z - 2"
z -= 2
print(z)
# "z += 2" VIENE A SER IGUAL A "z = z * 2"
z *= 2
print(z)
# "z += 2" VIENE A SER IGUAL A "z = z / 2"
z /= 2
print(z)

''' ********** USAMOS PEMDAS ************
P -> Paréntesis             D -> División
E -> Exponenciación         A -> Adición
M -> Multiplicacion         S -> Sustracción
''' 
print("********** PEMDAS *********")
operation_1 = 2 + 3 * 4
print(operation_1)

operation_2 = 2 + (3 * 4)
print(operation_2)

#SI LO HACEMOS CON LOS MISMOS DATOS QUE EL PRIMER EJEMPLO PERO CON PARENTESIS LAS SUMAS, NOS DATA OTRO RESULTADO
operation_3 = (2 + 3) * 4
print(operation_3)

operation_4 = (2+3) * (4**2) / 8 - 1
print(operation_4)


