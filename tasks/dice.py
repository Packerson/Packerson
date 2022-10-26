import random

possible_dice = ("D100", "D20", "D10", "D8", "D6", "D4", "D3")


# XDY+Z

def dice(formula):
    multiply = None
    new_formula = None
    dice_value = None
    x = 0
    for dice_1 in possible_dice:
        if dice_1 in formula:
            try:
                multiply, new_formula = list(formula.split(dice_1))
            except ValueError:
                print("wrong formula")
            dice_value = int(dice_1[1:])
            # From D100 take only number (100), taking second parametr from list
            break
        else:
            pass
    try:
        # Check value of X, if there is nothing x = 1
        if len(multiply) == 0:
            multiply = 1
        elif type(int(multiply)) == int:
            multiply = int(multiply)
    except (ValueError, TypeError):
        return "wrong formula 2"
    # Check value of Z!
    try:
        if len(new_formula) == 0:
            new_formula = 0
        elif type(int(new_formula)) == int:
            new_formula = int(new_formula)
    except ValueError:
        return "something wrong"
    # each dice roll can be difrent, sum everthing
    for i in range(multiply):
        x = random.randint(1, dice_value) + x
        print(x)

    roll_dice = x + new_formula
    return roll_dice


print(dice("D6D6"))
