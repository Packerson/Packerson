def find_it(array):
    new_array = []
    [new_array.append(i) for i in array if array.count(i) % 2 == 1]
    return new_array[0]

# def find_it(array):
#     new_array = []
#     # for i in array:
#     #     if array.count(i) % 2 == 1:
#     #         new_array.append(i)
#     #         print(new_array)
#     return [new_array.append(i) for i in array if array.count(i) % 2 == 1][0]
#     # return new_array[0]


find_it([1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1])
