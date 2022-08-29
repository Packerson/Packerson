x = int(input("Podaj liczbę elementów: "))
numbers = []
for loop1 in range(x):
    y = input("Podaj element: ")
    numbers.append(y)
print(numbers)


def find_boundaries(numbers):
    M_max = None
    najmniejsza = None
    if len(numbers) == 0:
        a = None
    else:
        for i in numbers:
            if type(i) == int or type(i) == float:
                if najmniejsza == None or i <= najmniejsza:
                    najmniejsza = i
                if M_max == None or i >= M_max:
                    M_max = i
        a = (najmniejsza, M_max)
    return a


b = (find_boundaries(numbers))
print(b)
