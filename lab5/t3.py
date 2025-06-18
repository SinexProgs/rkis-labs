import random


length = int(input("Enter length of an array: "))
arr = []
prev_num = 0
for i in range(length):
    prev_num = random.randint(prev_num + 1, prev_num + 50)
    arr.append(prev_num)

print(f"Random incrementing array: {arr}")