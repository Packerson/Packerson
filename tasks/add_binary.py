def add_binary(a, b):
    c = int(a + b)
    result = []

    while c:
        result.append(c % 2)
        c = (c // 2)

    result.reverse()
    result = (''.join(str(x) for x in result))
    print(result)
    return result


add_binary(50, 10)


