def sum_number(a, b):
    result_sum = a + b
    return result_sum


def subtract(a, b):
    result = a - b
    return result


def add_and_subtract(a, b, c):
    sum = sum_number(a, b)
    res = subtract(sum, c)
    return res


a = int(input())
b = int(input())
c = int(input())

print(add_and_subtract(a, b, c))
