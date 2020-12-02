string = input()

number_string = string.split(" ")

numbers = []

for num in number_string:
    number = -int(num)
    numbers.append(number)

print(numbers)
