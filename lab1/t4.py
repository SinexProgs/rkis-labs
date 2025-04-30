def count_it(sequence):
    numbers = {}
    for num in sequence:
        cur_num = int(num)
        if cur_num in numbers.keys():
            numbers[cur_num] += 1
        else:
            numbers[cur_num] = 1
    first_num = -1
    first_count = 0
    second_num = -1
    second_count = 0
    third_num = -1
    third_count = 0
    for k, v in numbers.items():
        if v >= first_count:
            first_num, second_num, third_num = k, first_num, second_num
            first_count, second_count, third_count = v, first_count, second_count
    return {first_num: first_count, second_num: second_count, third_num: third_count}


print(count_it("48111620242832"))