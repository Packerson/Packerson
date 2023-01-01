def toolchanger(tools, startIndex, target):
    array_len = len(tools)
    index = tools.index(target)
    steps = []
    value_1 = startIndex - index
    value_2 = index - startIndex

    if abs(value_1) > abs(value_2) :
        steps.append(abs(value_2))
    elif abs(value_1) <= abs(value_2):
        steps.append(abs(value_1))
    elif array_len-startIndex + array_len - index:
        steps.append(array_len-startIndex + array_len - index)

    print(index)
    result = sorted(steps)
    return result[0]

print(toolchanger(["ballendmill", 'facemill', 'keywaycutter', 'slotdrill'],1, 'slotdrill'))