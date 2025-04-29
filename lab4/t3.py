from enum import Enum


class Operation(Enum):
    ADD = 1
    SUBTRACT = 2
    MULTIPLY = 3
    DIVIDE = 4


def calculate(a, b, op):
    result = 0
    match op:
        case Operation.ADD:
            result = a + b
        case Operation.SUBTRACT:
            result = a - b
        case Operation.MULTIPLY:
            result = a * b
        case Operation.DIVIDE:
            result = a / b
    return a, b, op, result


a = int(input("Enter number A: "))
b = int(input("Enter number B: "))
op_text = input("Enter operation (ADD, SUBTRACT, MULTIPLY, DIVIDE): ");
op = Operation[op_text.upper()]
print(calculate(a, b, op))