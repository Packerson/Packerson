def performOperations(arr, operations):
    for operation in operations:
        left_side = arr[0:operation[0]]
        print(left_side)
        right_side = arr[operation[1]:-1]
        print(right_side)
        mid = arr[operation[0]:operation[1]+1]
        revers_mid = mid[::-1]
        print(revers_mid)
        arr = left_side+revers_mid+right_side
        left_side = []
        right_side = []
        mid = []
        revers_mid = []
    return arr

print(performOperations([0,1,2,3,4,5,6,7,8,9],[[0,9],[4,5]]))