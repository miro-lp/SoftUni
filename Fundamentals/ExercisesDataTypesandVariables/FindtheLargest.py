number = input()

numbers = []

for i in number:
    numbers.append(int(i))
max_number = []

for i in range(len(numbers)):
    max_number.append(max(numbers))
    numbers.remove(max(numbers))

for i in max_number:
    print(i, end="")
