import os

# VARIABLE "cwd"(Current Working Directory)
# el "getcwd()" lo que hace es decirnos en que directorio estamos actualmente
# OBTENER EL DIRECTORIO ACTUAL
'''cwd =  os.getcwd()
print("Directorio de Trabajo Actual", cwd)'''

# LISTAR LOS ARCHIVOS .txt
txt_files = [f for f in os.listdir('./34.Libreria-OS-Math-Y-Random') if f.endswith('.txt')]
print("Archivos txt: " , txt_files)

# RENOMBRAR ARCHIVO
os.rename('./34.Libreria-OS-Math-Y-Random/pila.txt', './34.Libreria-OS-Math-Y-Random/pila-renombrada.txt')
print("ARCHIVO RENOMBRADO")


# LISTAR LOS ARCHIVOS .txt
txt_files = [f for f in os.listdir('./34.Libreria-OS-Math-Y-Random') if f.endswith('.txt')]
print("Archivos txt: " , txt_files)


