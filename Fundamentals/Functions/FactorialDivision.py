def factorial_division(num, div):
    factotial_result = 1
    for i in range(1, num + 1):
        factotial_result *= i
    factotial_div = 1
    for i in range(1,div+1):
        factotial_div *= i
    finall_num = factotial_result / factotial_div
    return finall_num


first_num = int(input())
second_num = int(input())

print(f"{factorial_division(first_num, second_num):.2f}")
