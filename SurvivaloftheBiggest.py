text = input().split(" ")
amount = int(input())

list_of_integer = []
for i in text:
    num = int(i)
    list_of_integer.append(num)

for _ in range(amount):
    min_number = 9999999
    for number in list_of_integer:
        if number < min_number:
            min_number = number

    list_of_integer.remove(min_number)

print(list_of_integer)
