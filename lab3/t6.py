def product_of_odd(arr):
    product = 1
    for i in range(1, len(arr), 2):
        product *= arr[i]
    return product

print(product_of_odd([1, 2, 3, 4, 5]))