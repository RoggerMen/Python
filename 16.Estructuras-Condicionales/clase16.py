# EL USO DEL "if" DEBE TENER una sentencia como condicion que si es verdadero que permita ejecutarla si es falsa NO LA EJECUTA
x = 10
x = 3
x = 5
if x > 5:
    print(f"X -> {x} es mayor que 5")
# USO DEL "elif" va acompañado tambien de una sentencia QUE TIENE QUE SER CONDICIONAL
elif x == 5 :
    print(f"X -> {x} es igual que 5")
    
# USO DEL "else"
else:
    print(f"X -> {x} es menor que 5")
print("Estamos afuera del if")




