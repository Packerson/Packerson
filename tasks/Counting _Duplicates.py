def duplicate_count(array):
    duplicate_elements = []
    array = array.lower()
    for i in range(len(array)):
        if array.count(array[i]) >= 2:
            if array[i] not in duplicate_elements:
                duplicate_elements.append(array[i])
    print(duplicate_elements)
    return len(duplicate_elements)


duplicate_count('abcdeaB')


def duplicate_count_2(text):
    count = 0
    for c in set(text.lower()):
        if text.lower().count(c) > 1:
            count += 1
    return count
