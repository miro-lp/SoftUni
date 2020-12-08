def smallest_number(a, b, c):
    min_number = 0
    if a <= b and a <= c:
        min_number = a
    elif b <= a and b <= c:
        min_number = b
    elif c <= a and c <= b:
        min_number = c
    return min_number


first_num = int(input())
second_num = int(input())
third_nun = int(input())

print(smallest_number(first_num, second_num, third_nun))
