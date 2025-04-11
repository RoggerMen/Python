''' *** Cuando a alguna "class str o list o etc"
    La queremos copiar por ej:
    a = [1,2,3,4,5]
    b = a
    TENEMOS QUE TENER EN CUENTA:
    Que no tan solo se copia informacion de la lista SINO que tambien se toma en cuenta la caracteristica fundamental QUE APUNTA AL ESPACIO EN MEMORIA donde se ESTA GUARDANDO ESTA INFORMACION, QUIERE DECIR:
    Todo lo que hagamos en la lista "a" SE VA A VER PLASMADO EN LA LISTA "b"
    **** Y SI NOSOTROS QUEREMOS COPIAR SOLO LA INFORMACION Y NO APUNTAR AL MISMO ESPACIO EN MEMORIA USAMOS EL "slice()"
'''
a = [1,2,3,4,5]
b = a
print(a)
print(b)

# CON ESTO QUEREMOS QUE ELIMINE SOLO EL "Primer elemento" DE "a"
# PERO COMO "b" COPIA EL MISMO ESPACIO EN MEMORIA QUE "a" ESTE TAMBIEN SE ELIMINA(OSEA AL ELIMINAR DE "a" SU ELEMENTO SALE "PERJUDICADO" EL ELEMENTO COPIADO DE "b")
del a[0]
print(a)
print(b)

# ESTAS TAMBIEN SE VEN POR EL "id" PARA VER SI ESTAN EN EL MISMO ESPACIO
print(id(a))
print(id(b))

# Y PARA NO TENER ESTOS PROBLEMAS QUE TODAS LAS ACCIONES QUE HAGAMOS EN UNA VARIABLE ORIGINAL DESPUES DE HABER SIDO COPIADA POR OTRA(ej. a =[1,2,3,4,5] , b = a) SEAN CAMBIADAS TAMBIEN, USAMOS EL "slice()"
# AQUI : "c" VA A SER IGUAL A LA INFORMACION QUE TENGO EN "a" PERO ESTA VES COPIAMOS CON [:] que esto quiere decir: TODO LO QUE VIENE DE LA "posicion 0(inicial)" HASTA LA "posicion final"
print("AQUI USAMOS SLICE CON LA VARIABLE 'c'")
c = a[:]
print(id(a))
print(id(b))
print("\nAQUI VEMOS QUE HAY CAMBIOS DE ESPACIO EN MEMORIA USANDO EL 'SLICE', Y USAMOS DIFERENTES ESPACIOS EN MEMORIA")
print(id(c))
print("\nAQUI VERIFICAMOS QUE NO TENEMOS EL MISMO PROBLEMA DE 'b' COPIADO POR 'a' que con 'c' AL USARLO CON 'slice()'")
print("\nAl agregar a 'a' con 'append(6)' UN ELEMENTO MAS ESTE TAMBIEN AGREGARIA A 'b' MAS YA NO A 'c'")
a.append(6)
print(id(a))
print(id(b))
print(id(c))

