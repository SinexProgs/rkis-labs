arr = []
while True:
    input_string = input()
    if len(input_string) == 0:
        break
    arr.append(input_string)

shortest_str = arr[0]
longest_str = arr[0]
for i in range(1, len(arr)):
    cur_str = arr[i]
    cur_len = len(cur_str)
    if cur_len > len(longest_str):
        longest_str = cur_str
    if cur_len < len(shortest_str):
        shortest_str = cur_str

print("Shortest string:", shortest_str)
print("Longest string:", longest_str)