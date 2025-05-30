import ast
import math


def get_sum_and_product(arr):
    sum_of_positives = 0
    for x in arr:
        if x > 0:
            sum_of_positives += x

    min_index = 0
    min_value = arr[0]
    max_index = 0
    max_value = arr[0]
    for i in range(1, len(arr)):
        cur_value = arr[i]

        if cur_value < min_value:
            min_index = i
            min_value = cur_value

        if cur_value > max_value:
            max_index = i
            max_value = cur_value

    if min_index < max_index:
        nums_between_min_max = arr[min_index + 1:max_index]
    else:
        nums_between_min_max = arr[max_index + 1:min_index]

    product_between_min_max = math.prod(nums_between_min_max)

    return sum_of_positives, product_between_min_max


arr = ast.literal_eval(input("Enter numbers (in square brackets): "))
result = get_sum_and_product(arr)
print(f"Sum of positive numbers: {result[0]}")
print(f"Product of numbers between min and max: {result[1]}")