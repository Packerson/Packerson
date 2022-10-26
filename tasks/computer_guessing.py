# zchange too_small, too_big for 1 , 2
def guess():
    print("Think about number from range 1-1000,  Computer will guess it in 10 rounds!")
    min_number = 0
    max_number = 1000
    for i in range(10):
        print(f"{10 - i} rounds left")
        guess_number = int(max_number - min_number) / 2 + min_number
        print(f"I guess {guess_number}")
        answer = input("Write your answer: too_big, too_small, you_won:\n")
        print(answer)
        if answer == "you_won":
            return "Congratuluation YOU WON!!"
        elif answer == "too_big":
            max_number = guess_number
            print("i will try again-1")
        #    print(f"{10-i} round left")
        elif answer == "too_small":
            min_number = guess_number
            print("i will try again-2")
        #    print(f"{10 - i} round left")
        else:
            print("dont cheat!")
    return "Dont cheat"


print(guess())
