arr = [-21, 0, -4, -12, 24, 4, 32, -8, 21, 10]
new_arr = []

for x in arr:
    if 9 < x < 100:
        new_arr.append(x)
new_arr.sort()

print(f"Original array: {arr}")
print(f"Filtered array: {new_arr}")