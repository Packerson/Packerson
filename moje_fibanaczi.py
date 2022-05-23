#ciąg fibanacziego dla n wyrazów
def fiban(n):
    a = 0
    b = 1
    print("wyraz", 1, a)
    print("wyraz", 2, b)
    for i in range(1, n - 1):
        a, b = b, a + b
        print("wyraz", i + 2, b)
    return b

a=fiban(10)
print(a)


def fib_iter2(n):
    """
        Funkcja drukuje kolejne wyrazy ciągu Fibonacciego
        aż do wyrazu n-tego, który zwraca.
        Wersja iteracyjna z pętlą for.
    """
    a, b = 0, 1
    print("wyraz", 1, a)
    print("wyraz", 2, b)
    for i in range(1, n - 1):
        # wynik = a + b
        a, b = b, a + b
        print("wyraz", i + 2, b)

    print()  # wiersz odstępu
    return b

b=fib_iter2(5)
print(b)


def fibb(n):
    result = [0, 1]
    for i in range(n-2):
        result.append(result[i] + result[(i + 1)])

    return result

c=fibb(8)
print(c)