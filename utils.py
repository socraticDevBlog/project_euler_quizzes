def splitArrayBySize(arr, size):
    arrs = []
    while len(arr) > size:
        pice = arr[:size]
        arrs.append(pice)
        arr = arr[1:]
    arrs.append(arr)
    return arrs


def stringToIntArray(string_input):
    return [int(i) for i in str(string_input)]
