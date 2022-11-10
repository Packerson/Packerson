def solution(number):

    suma = 0
    if number < 0:
        return 0

    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            suma += i
    return suma
