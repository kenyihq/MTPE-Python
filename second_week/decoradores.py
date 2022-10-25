# Exercise 1

def func_main(func_avg:float):
    def func_sec(get_avg:float):
        if len(get_avg) != 0:
            return func_avg(get_avg)
        return "Lista vacía"
    return func_sec


@func_main
def promedio(my_list:list) -> float:
    return round(sum(my_list)/len(my_list), 2)


# lista = [12,243,42]
# print(promedio(lista))







def run():
    print("EJERCICIOS CON DECORADORES")
    option = int(input("\nElija el número de ejercicio entre el 1 y el 5: "))

    while option > 0 and option < 6:
        if option == 1:
            len_list = int(input("Ingrese la longitud de su lista: "))
            lista = []
            for i in range(len_list):
                j = f"Ingrese el {i+1} elemento de la lsita: "
                lista.append(j)

            promedio(lista)
        


if __name__ == '__main__':
    run()