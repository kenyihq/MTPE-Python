'''
Pregunta 3
Escriba un programa de Python para listar todos los archivos en un directorio en Python. (por precaución que sea en una carpeta temporal y que no contenga archivos importantes, coloque copias)
'''

import os
from pickletools import read_uint1

def get_list(my_path):
    my_directory = os.listdir(my_path)
    # print(type(my_directory))

    with open("listar.txt", "w", encoding="utf8") as file:
        for row in my_directory:
            file.write(f"{row}\n")

    return "Exito, se creo un archivo TXT con el listado deseado"

'''
Pregunta 5
Escriba un programa en Python para calcular el número de días entre dos fechas. No es necesario que use inputs para el ingreso de las fechas
'''

from datetime import datetime

def calc_days(day_1, day_2):

    first_day = datetime.strptime(day_1, '%Y-%m-%d')
    second_day = datetime.strptime(day_2, '%Y-%m-%d')

    total_days = first_day-second_day
    return total_days.days


'''
Pregunta 6
Desarrolle un función que lea el archivo y que de la columna QuotaAmount, calcule el promedio de los valores para luego retornarlo.
'''

import csv

def read_data(new_csv):
    with open(new_csv, 'r', encoding='utf-8') as csvfile:
        data = csv.reader(csvfile)

        quota_amount = [int(row[0]) for row in data if row[0].isnumeric()]
        av_qa = round(sum(quota_amount)/len(quota_amount), 2)

        return av_qa

'''
Pregunta 7
Del ejercicio anterior cree dos pruebas unitarias (use unittest), una que compare el valor de retorno con "146633.33" y el otro con "15000", ambos test deben dar "Ok" como salida.

Recuerde usar la palabra "test" al inicio de cada función con su prueba.
'''

import unittest

class Exercise7(unittest.TestCase):
    
    def test_exercise_7(self):
        self.assertEqual(read_data('./dataset/gumjjcpx.txt'), 146633.33)

    def test_exercise_7b(self):
        self.assertEqual(read_data('./dataset/gumjjcpx.txt'), 15000)


def run():
    print("Taller de standard library")
    option = int(input("Elija el ejercicio a ejecutar: "))

    if option == 3:
        my_path = input("Ingrese el directorio que desea listar: ")
        print(get_list(my_path))

    elif option == 5:
        day_1 = input("Ingrese la primera fecha: ")
        day_2 = input("Ingrese la segunda fecha: ")

        print(calc_days(day_1, day_2))


    elif option == 6:
        print(read_data('./dataset/gumjjcpx.txt'))

    elif option == 7:
        unittest.main()


    else:
        print("No realice ese ejercicio 😢")



if __name__ == '__main__':
    run()