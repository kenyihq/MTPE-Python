'''
Pregunta 1
Implementar la función get_avg que calcule el promedio de una lista de números:

def get_avg(lista):
  lista = [10, 40, 20, 45, 25, 35, 15]
  pass
La función get_avg retorna un float.

Asimismo implementar un decorador que permita imprimir los siguientes mensajes:

Inicio del cálculo del promedio de la lista de números.
El cálculo ha finalizado.
Entre ambos mensajes debe realizarse el cálculo del promedio de números.
'''

def get_avg(my_list:list) -> float:
    total : int = 0
    for i in my_list:
        total += i

    return round(total/len(my_list), 2)

lista = [10, 40, 20, 45, 25, 35, 15]

print(get_avg(lista))

'''
Pregunta 2
Escriba un programa que dada una entrada numérica por el usuario, ingrese a una función que duplique el valor y sea retornado en forma de string o cadena. Utilice tipos tanto para las variables como para las funciones.
'''

def exercise_2(num:int) -> str:
    return str(num*2)

example = int(input("Ingrese un número: "))
print(exercise_2(example))


'''
Pregunta 3
Cree una función con anotaciones, que tome una palabra y duplique sus letras y las retorne en una lista.

Ejemplo:

Ingrese una palabra: hola

Retorna: ['h','h','o','o','l','l','a','a']
'''

def exercise_3(word:str) -> list:
    my_list : list = []
    for i in word:
        my_list.append([j*2 for j in i])
        # my_list.append(i)

    return my_list

h = 'Hola'
print(exercise_3(h))