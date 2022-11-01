def descending_order(num):

    num_list = list(str(num))
    counter = 1
    temp = 0
    swap = True

    # if len(num_list) == 2:
    #     if num_list[0] <= num_list[1]:
    #         num_list[0], num_list[1] = num_list[1], num_list[0]
    #         return int("".join(num_list))
    """Bubble sorted"""
    while swap:
        swap = False
        for i in range(len(num_list)-1-temp):
            counter += 1
            if num_list[i] < num_list[i+1]:
                num_list[i], num_list[i+1] = num_list[i+1], num_list[i]
                swap = True
        temp += 1
    num2 = int("".join(num_list))
    print(f"counter = {counter}")
    return num2


print(descending_order(123456789))


def descending_order_2(num):
    num2 = list(str(num))
    new_num = sorted(num2, reverse=True)
    a_new_num2 = "".join(new_num)
    return a_new_num2

print(descending_order_2(15))
