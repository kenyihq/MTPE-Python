list_1 = ["a", "b", "c"]
list_2 = [1, 2, 3]

for cont, value in enumerate(zip(list_1, list_2), start=1):
    print(cont, "->", value)