arr = [-2, 0, -4, -1, 2, 4, 3, -8, 2, 0]
print(f"Numbers: {arr}")
for num in arr:
    if num > 0:
        print(f"First positive number: {num}")
        break
for num in reversed(arr):
    if num < 0:
        print(f"Last negative number: {num}")
        break