'''
Ejercicio 3
Escriba un programa de Python para listar todos los archivos en un directorio en Python. (por precaución que sea en una carpeta temporal y que no contenga archivos importantes, coloque copias)
'''

import os

my_directory = os.listdir('./')
print(type(my_directory))

with open("listar.txt", "w", encoding="utf8") as file:
    for row in my_directory:
        file.write(f"{row}\n")
