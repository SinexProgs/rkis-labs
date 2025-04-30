def change(lst):
    lst[0], lst[-1] = lst[-1], lst[0]


lst = [4, 8, 12, 16, 20, 24, 28, 32]
print("Original list:", lst)
change(lst)
print("Changed list:", lst)