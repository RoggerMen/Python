# ******** BUCLES Y CONTROL DE ITERACIONES ******
# Solo con "for"
numbers = [1,2,3,4,5,6]
for i in numbers:
    print("Aquí i es igual a: ", i)


# DE OTRA MANERA ES TAMBIEN USANDO EL "for in range"    
for i in range(3,10):
    print(i)

# RECCORER POR ELEMENTO "for in"
fruits = ["manzana","pera", "uva", "naranja", "plátano"]

for fruta in fruits:
    print(fruta)
    if fruta == "naranja":
        print("Naranja  encontrada")
    if fruta == "plátano":
        print("plátano encontrado")
        


# BUCLE CON "while" 

# USAMOS LA PALABRA RESERVADA "break" PARA HACER UN PARE(stop/parar) OSEA EL CODIGO TERMINA CON EL "break"
x = 0
while x < 5:
    if x == 3:
        break
    print(x)
    x += 1

# USAMOS LA PALABRA RESERVADA "continue" PARA SALTAR U OMITIR EL PASO QUE QUEREMOS EVALUAR Y QUE SIGA CON LO QUE TENGA QUE SEGUIR

numbers = [1,2,3,4,5,6]
for i in numbers:
    if i == 3:
        continue
        # break
    print("Aquí i es igual a: ", i)


