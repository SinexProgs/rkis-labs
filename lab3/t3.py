def count_squares_in_rect(rect_w, rect_h, sqr_s):
    return int((rect_w // sqr_s) * (rect_h // sqr_s))


rect_w = float(input("Enter the width of the rectangle: "))
rect_h = float(input("Enter the height of the rectangle: "))
sqr_s = float(input("Enter the size of the square: "))

print(count_squares_in_rect(rect_w, rect_h, sqr_s), "squares in rectangle")