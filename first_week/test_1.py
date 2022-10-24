m = [[1,2,3],[4,5,6],[7,8,9]]
n = 0

def extrae_column_n(list_column, column):
    if column >= 0 and column < len(list_column):
        return list_column[column]

    else:
        return []

#print(extrae_column_n(m,n))




def test_1(a,b):
    c = []
    for i in a:
        if i == b[0]:
            if i+1 == b[1]:
                if i+2 == b[2]:
                    return f"{b[0]}{b[1]}{b[2]}"


    # return c
a = 'abbbccda'
b = 'bbc'

print(test_1(a,b))