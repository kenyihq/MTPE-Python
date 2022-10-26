'''
Pregunta 1
Dada la lista de notas [15,20,18] y la lista de alumnos ["Marcelo", "José", "Juan"] Imprimirlos de la siguiente forma:

Marcelo : 15

José : 20

Juan : 18
'''

from turtle import st


def notes(names:list, notes:list):
    for i,j in zip(names, notes):
        print(i, ":", j)

list_names = ["Marcelo", "José", "Juan"]
list_notes = [15, 20, 18]

notes(list_names, list_notes)


'''
Pregunta 2
Dada la siguiente lista ['Hola', True, 5, 6.04]

Imprimir los valores e índices sin utilizar un contador o range.

0 -> Hola
1 -> True
2 -> 5
3 -> 6.04
'''


def exercise_2(new_list:list):
    for i, j in enumerate(new_list, start=0):
        print(i, "->", j)

my_list = ['Hola', True, 5, 6.04]

exercise_2(my_list)

'''
Pregunta 3
Dada la lista de notas [15,20,18] y la lista de alumnos ["Marcelo", "José", "Juan"], imprimirlos de la siguiente forma:

1 -> Jose : 20

2 -> Juan : 18

3 -> Marcelo : 15

No usar range, ni comparadores. Hint: usar sorted
'''



'''
Pregunta 4
Escriba un generador que permita contar las letras de las palabras de una lista.

Ejemplos:

Para "humanidad": {'h': 1, 'u': 1, 'm': 1, 'a': 2, 'n': 1, 'i': 1, 'd': 2}

Para "humano": {'h': 1, 'u': 1, 'm': 1, 'a': 1, 'n': 1, 'o': 1}
'''



'''
Pregunta 5
Teniéndos los siguientes criterios:

Desaprobado: nota < 11
Destacado: nota > 16
Aprobado: para el resto de casos
notas = [15, 20 18, 11, 4, 7, 14, 13 ,1 ,9, 10]
alumnos = ["Marcelo", "Jose", "Juan", "Marco", "María", "Ricardo", "Liz", "Diego", "Roberto", "Martin", "Álvaro"]
alumnos_notas = zip(alumnos, notas)

def registrar_aprobados(l):
    pass
Implementar registrar_aprobados como generador y que su único parametro de entrada sea alumnos_notas Posteriormente utilizar un bucle y enumerate para obtener la siguiente salida.

1 -> Marcelo : 15 (Aprobado)
2 -> Jose : 20 (Destacado)
3 -> Juan : 18 (Destacado)
4 -> Marco : 11 (Aprobado)
5 -> María : 4 (Desaprobado)
6 -> Ricardo : 7 (Desaprobado)
7 -> Liz : 14 (Aprobado)
8 -> Diego : 13 (Aprobado)
9 -> Roberto : 1 (Desaprobado)
10 -> Martin : 9 (Desaprobado)
11 -> Álvaro : 10 (Desaprobado)
'''

def registrar_aprobados(new_tuple):
    for student, notes in new_tuple:

        if notes < 11:
            qualification = f'{student} : {notes} (Desaprobado)'
            yield qualification

        elif notes > 16:
            qualification = f'{student} : {notes} (Destacado)'
            yield qualification

        else:
            qualification = f'{student} : {notes} (Aprobado)'
            yield qualification


    return qualification
    # for num, alm in enumerate(qualification, start=0):
    #     print(num, '->', alm)


notas = [15, 20, 18, 11, 4, 7, 14, 13 ,1 ,9, 10]
alumnos = ["Marcelo", "Jose", "Juan", "Marco", "María", "Ricardo", "Liz", "Diego", "Roberto", "Martin", "Álvaro"]
alumnos_notas = zip(alumnos, notas)

test = registrar_aprobados(alumnos_notas)
for number, student in enumerate(test, start=1):
    print(number, '->', student)



# print(registrar_aprobados(alumnos_notas))