def filter_list(array):
    digit_array = []
    [digit_array.append(a) for a in array if isinstance(a, int)]

    return digit_array


filter_list([1, 2, 'aasf', '1', '123', 123])
