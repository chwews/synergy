def find_minmax_indexes(arr):
    if len(arr) == 0:
        raise ValueError('Input array is empty')

    min_value = arr[0]
    max_value = arr[0]
    min_index = 0
    max_index = 0
    for ind, val in enumerate(arr):
        if val > max_value:
            max_value = val
            max_index = ind
        if val < min_value:
            min_value = val
            min_index = ind

    return min_index, max_index


def find_negative_sum(arr, inclusive=True):
    if len(arr) == 0:
        return 0

    if len(arr) < 2:
        if arr[0] < 0:
            return arr[0]
        else:
            return 0

    min_index, max_index = find_minmax_indexes(arr)

    start, end = max_index, min_index
    if min_index < max_index:
        start, end = end, start

    if not inclusive:
        start += 1
        end -= 1

    negative_sum = 0
    while start <= end:
        if arr[start] < 0:
            negative_sum += arr[start]
        start += 1

    return negative_sum
