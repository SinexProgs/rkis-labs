def find_min(arr):
    min_value = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < min_value:
            min_value = arr[i]
    return min_value


print(find_min([5, 7, 2, 4, 1, -1]))