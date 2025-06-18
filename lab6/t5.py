c = input("Enter C: ")
a_arr = ["a", "part", "falling", "pup", "miss", "area", "eerie", "holpen", "ease", "noon"]
count = 0

for a in a_arr:
    if len(a) > 1 and a.startswith(c) and a.endswith(c):
        count += 1

print(f"Count of matching A's: {count}")