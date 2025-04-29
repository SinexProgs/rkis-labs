def are_digits_descending(num):
    prev_digit = num % 10
    num //= 10
    while num > 0:
        cur_digit = num % 10
        if cur_digit <= prev_digit:
            return False
        num //= 10
    return True


print(are_digits_descending(963))
print(are_digits_descending(845))
