def calculate_formula(a, b):
    return (a + 4 * b) * (a - 3 * b) + a * 2

a = float(input("Enter A: "))
b = float(input("Enter B: "))
print(f"Result: {calculate_formula(a, b)}")