from itertools import combinations


def choose_best_sum(t, k, ls):
    ls = [50, 55, 57], [50, 55, 58], [50, 55, 60], [50, 57, 58], [50, 57, 60], [50, 58, 60], [55, 57, 58], [55, 57, 60], \
        [55, 58, 60], [57, 58, 60]
    # k = towns
    # t = distance
    # ls = list of distance between towns
    distance = 0
    # thanks combinations can find all combinations in list
    for x in combinations(ls, k):
        if sum(x) <= t:
            distance = max(distance, sum(x))

    if distance == 0:
        return None
    return distance
