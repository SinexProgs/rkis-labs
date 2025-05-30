import ast


arr = ast.literal_eval(input("Enter numbers (in square brackets): "))
for i in range(len(arr)):
    arr[i] *= -1
print(f"Inverted array: {arr}")