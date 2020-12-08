def odd_even_sum(number):
    odd_sum = 0
    even_sum = 0
    for i in number:
        if int(i) % 2 == 0:
            even_sum += int(i)
        else:
            odd_sum += int(i)
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


num = input()

print(odd_even_sum(num))
