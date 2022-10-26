import random


def roll_the_dice(throw_str):
    if throw_str.count('D') != 1:
        return f'Niepoprawny format rzutu {throw_str}'
    else:
        number_of_throws, temp = throw_str.split('D')

    if '+' in temp:
        type_of_dice, modification = temp.split('+')
    elif '-' in temp:
        type_of_dice, modification = temp.split('-')
        modification = '-' + modification
    else:
        modification = 0
        type_of_dice = temp

    if type_of_dice not in ['2', '3', '4', '6', '8', '12', '20', '10', '100']:
        return f'Niepoprawny rodzaj kości. {type_of_dice}'

    if number_of_throws == '':
        number_of_throws = 1
    elif number_of_throws.isdigit():
        number_of_throws = int(number_of_throws)
    else:  # Dla ilości rzutów nie będącej pustym napisem(niepodana) lub liczbą zwracamy wyjątek
        return f'Niepoprawna ilość rzutów. {number_of_throws}'

    result = 0
    for i in range(number_of_throws):
        result += random.randint(1, int(type_of_dice))

    try:
        result += int(modification)
    except ValueError:
        return f'Niepoprawny modyfikator rzutu. {modification}.'

    return result


if __name__ == '__main__':
    # user_input = input('Wprowadź wyrażenie rzutu kośćmi: ')
    print(roll_the_dice("2D10+10"))
    print(roll_the_dice("D6"))
    print(roll_the_dice("2D3"))
    print(roll_the_dice("D12-1"))
    print(roll_the_dice("DD34"))
    print(roll_the_dice("4-3D6"))
    print(roll_the_dice("D6D6"))