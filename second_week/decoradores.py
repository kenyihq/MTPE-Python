def func_main(func_avg:float):
    def func_sec(get_avg:float):
        if len(get_avg) != 0:
            print("Se inicia el cálculo")
            return func_avg(get_avg)
        else:
            print("Lista vacía")
            return

    return func_sec


@func_main
def promedio(my_list:list) -> float:
    print(sum(my_list)/len(my_list))


lista = [12]
promedio(lista)