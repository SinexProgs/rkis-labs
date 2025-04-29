x = int(input("Enter x:"))
arr = [39, 36, 33, 30, 27, 24, 21, 18, 15, 12, 9, 6, 3]
x_in_arr = False
for i in arr:
    if i == x:
        x_in_arr = True
        break
print(f"{x} is in {arr}" if x_in_arr else f"{x} is not in {arr}")
