def count_pos_in_arr(arr):
    count = 0
    for num in arr:
        if num >= 0:
            count += 1
    return count

print(count_pos_in_arr([-1, 0, 1, 2, -1, -4]))