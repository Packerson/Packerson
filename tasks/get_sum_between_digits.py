def get_sum(a, b):
    summary = 0
    if a == b:
        return a
    if a > b:
        array = list(range(b, a))
    else:
        array = list(range(a, b))
    for i in array:
        summary += i

    return summary


get_sum(0, -1)
