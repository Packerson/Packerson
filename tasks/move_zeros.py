def move_zeros(array):
    counter = array.count(0)
    for i in range(counter):
        array.remove(0)
        array.append(0)

    return array

move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1])
