numbers = [5, 14, "-14", 15, 14, 17, 18, "19", None, "12", "kuku"]


def find_boundaries(moja_lista):
    M_max = None
    najmniejsza = None
    if len(moja_lista) == 0:
        a = None
    else:
        for i in moja_lista:
            if type(i) == int or type(i) == float:
                if najmniejsza == None or i <= najmniejsza:
                    najmniejsza = i
                if M_max == None or i >= M_max:
                    M_max = i
        a = (najmniejsza, M_max)
    return a


b = find_boundaries(numbers)
print(b)
