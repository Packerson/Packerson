import random


def guess_number(n):
    n = random.randint(1, 100) #random number
    new = 0
    while n != new:
        new = input("Guess number:")
        try:
            if new.isdigit() == False: #checking value
                print("It is not a number!\nTry again")
                new = input("Guess number:")
            if type(int(new)) == int:
                new = int(new)
                if n == new:
                    return ("You won")
                elif n > new:
                    print("Too small!")
                else:
                    print("Too big")
        except ValueError: #safety for non numbers marks like:,./?
            print("It is not a number!\nTry again")
            new = input("Guess number:")


print(guess_number(4))
