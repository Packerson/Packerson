import random


def my_list():  # creat my lotto numbers
    my_num_list = []
    print("Give 6 numbers from 1-49")
    for i in range(1, 15):
        if (len(my_num_list)) < 6:  # checking len of your list number
            my_new_number = (input("Give a number: "))
            if my_new_number.isdigit() == True:  # checking valoue numbers
                if type(int(my_new_number)) == int:
                    my_new_number = int(my_new_number)
                    if my_new_number in range(1, 50):  # check range
                        if my_new_number in my_num_list:  # check repeating
                            print("Numbers cannot be repeted")
                        else:
                            my_num_list.append(my_new_number)
                    else:
                        print("number out of range")
                else:
                    print("It is not a number")
            else:
                print("It is not a number!!")
    my_num_list = sorted(my_num_list)  # sort

    return my_num_list

    # lotto_numbers = [random.randrange(1, 49, 1) for i in range(6)]  #creat new random lotto list,


def winning_numbers():  # creat winning numbers
    lotto_numbers = [i for i in range(1, 49)]
    random.shuffle(lotto_numbers)  # shuffle
    lotto_numbers = lotto_numbers[0:6]
    lotto_numbers = sorted(lotto_numbers)

    return lotto_numbers


def compare():  # compare two lists
    lotto_numbers = winning_numbers()
    my_num_list = my_list()
    won_list = [i for i in lotto_numbers if i in my_num_list]  # comparing two lists mozna by uzyc funkcji INTERSECTION
    if len(won_list) >= 3:
        return f"Your numbers: {my_num_list} \nLotto numbers: {lotto_numbers}, \nYou hit {len(won_list)} numbers, Winning numbers: {won_list}"
    else:
        return f"Your numbers: {my_num_list} \nLotto numbers: {lotto_numbers}, You didnt won :("


print(compare())
