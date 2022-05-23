numbers = [i for i in range(1, 20)]
print(numbers)
liczby = (i for i in range(1, 1000) if i % 5 == 1)
print(liczby)


def find_first_find_last(moja_lista):
    moja_lista = tuple(moja_lista)
    result = (moja_lista[0], moja_lista[-1])
    return result


b = find_first_find_last(numbers)
print(b)
b = find_first_find_last(liczby)
print(b)
