import operator


def solve_calculation(a, b, operator):
    result = None
    if operator == "multiply":
        result = a * b
    elif operator == "add":
        result = a + b
    elif operator == "divide":
        result = a // b
    elif operator == "subtract":
        result = a - b
    return result


operator: str = input()
first_num: int = int(input())
second_num: int = int(input())

result = solve_calculation(first_num, second_num, operator)
print(result)
