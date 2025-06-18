arr = [-2, 0, -4, -1, 2, 4, 3, -8, 2, 0]
pos_num = 0
neg_num = 0
for num in arr:
    if num > 0:
        pos_num = num
        break
for num in reversed(arr):
    if num < 0:
        neg_num = num
        break

print(f"First positive number: {pos_num}")
print(f"Last negative number: {neg_num}")