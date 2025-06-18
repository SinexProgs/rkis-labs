arr = [-21, 0, -4, -12, 24, 4, 32, -8, 21, 10]
new_arr = []

for x in arr:
    if x > 0:
        new_arr.append(x)

print(f"Original array: {arr}")
print(f"Filtered array: {new_arr}")