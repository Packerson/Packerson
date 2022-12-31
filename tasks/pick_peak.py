
# should return {pos: [3, 7], peaks: [6, 3]} (or equivalent in other languages)
# All input arrays will be valid integer arrays (although it could still
# be empty), so you won't need to validate the input.
# The first and last elements of the array will not be considered as peaks
# (in the context of a mathematical function, we don't know what is after
# and before and therefore, we don't know if it is a peak or not).
# Also, beware of plateaus !!! [1, 2, 2, 2, 1] has a peak while
# [1, 2, 2, 2, 3] does not. In case of a plateau-peak, please only
# return the position and value of the beginning of the plateau.
# For example: pickPeaks([1, 2, 2, 2, 1]) returns {pos: [1], peaks: [2]}
# (or equivalent in other languages)

def pick_peaks(arr):
    pos = []
    peaks = []
    for i in range(1, len(arr) - 1):
        number = arr[i]
        if number > arr[i - 1]:
            for a in range(i + 1, len(arr)):
                if number > arr[a]:
                    pos.append(i)
                    peaks.append(arr[i])
                    break
                elif number == arr[a]:
                    pass
                else:
                    break

    return {
        'pos': pos,
        'peaks': peaks
    }

print(pick_peaks([1, 2, 3, 6, 4, 1, 2, 3, 2,8, 1]))
