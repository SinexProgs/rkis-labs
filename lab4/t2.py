arr = []
arr_sum = 0
for i in range(14):
    cur_num = int(input())
    arr.append(cur_num)
    arr_sum += cur_num

arr.append(arr_sum)

for n in arr:
    print(n)