# ******** ITERADORES **********
# Ir iterando cada uno de los elementos pero sin utilizar indices
# Creamos una lista
my_list = [1,2,3,4]

# Obtenemos el iterador
# Con esto hacemos que itere desde el inicio de la lista cada que vaya acompañado del "next"
# Solo llega hasta la ultima iteración segun su último elemento. Este ya no vuelve a repetirse si generamos más de lo debido, NOS DARIA UN ERROR DE "StopIterator"
my_iter = iter(my_list)


# Usar el iterador
# "next" nos va a ayudar a que nosotros podamos ir viendo, cuales son los valores que se van guardando o almacenando en memoria
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

# UNO DE MAS NOS DARIA "ERROR" "StopIterator"
#print(next(my_iter))


