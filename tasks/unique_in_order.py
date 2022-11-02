def unique_in_order(iterable):
    new_i = list(iterable)
    counter_list = []

    for i in range(len(new_i) - 1):
        if new_i[i] == new_i[i + 1]:
            counter_list.append(i)

    counter_list.reverse()

    for i in counter_list:
        new_i.pop(i)

    return new_i


unique_in_order('AAAABBBCCDAABBB')
