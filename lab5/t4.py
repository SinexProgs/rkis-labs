my_str = input("Enter a string: ")

if my_str.startswith("abc"):
    my_str = "www" + my_str[3:]
else:
    my_str += "zzz"

print(f"New string: {my_str}")