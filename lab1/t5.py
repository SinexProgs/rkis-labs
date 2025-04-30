def sieve(lst):
    numbers = []
    for num in reversed(lst):
        if num not in numbers:
            numbers.append(num)
    return tuple(numbers)


lst = [4, 8, 4, 16, 20, 8, 28, 32, 32, 32, 4]
print(sieve(lst))