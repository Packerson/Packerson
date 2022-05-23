def chessboard(n):
    empty = ''

    for i in range(n):
        if i % 2:
            empty += " #" * (int(n / 2))
            if i % 2:
                empty += " "
            empty += "\n"
        else:
            empty += "# " * (int(n / 2))
            if n % 2:
                empty += "#"
            empty += '\n'

    return empty


a = chessboard(4)
print(a)

print("druga wersja")


def chessboard_2(n=8):
    result = ''
    for i in range(n):
        if i % 2:
            result += " #" * (int(n / 2))
            if n % 2:
                result += " "
                result += "\n"
        else:
            result += "# " * (int(n / 2))
            if n % 2:
                result += "#"
            result += "\n"
    return result


c = chessboard_2(1)
print(c)

