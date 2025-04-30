import random


arr = [0] * 10
for i in range(10):
    arr[i] = random.randint(0, 100)
print(min(arr))