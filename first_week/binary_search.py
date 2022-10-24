import random

def binary_search(list1, n):
    low = 0
    high = len(list1) - 1
    mid = 0

    while low <= high:
        mid = (high + low ) // 2

        if list1[mid] < n:
            low = mid + 1
    
        elif list1[mid] > n:
            high = mid - 1

        else:
            return mid

    return -1

list1 = []

elementos = int(input("Cuantos elementos quieres? "))

for i in range(elementos):
    list1.append(random.randrange(1, 100))

list1.sort()
print(list1)

n = int(input("Que numero deseas buscar? "))

result = binary_search(list1,n)

if result != -1:
    print("Elemento se encuentra en el indice", str(result))
else:
    print("Elemento no se encuentra en la lista")