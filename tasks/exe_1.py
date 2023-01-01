

def stockPairs(stocksProfit, target):
    from itertools import combinations
    counter = 0
    value = 0
    for x in combinations(stocksProfit, 2):
        if sum(x) == target:
            counter += 1
            value = max(value, sum(x))

    if value == 0:
        return
    return counter
