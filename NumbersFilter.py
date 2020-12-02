n = int(input())

list_numbers = []
filter_list = []

for i in range(n):
    number = int(input())
    list_numbers.append(number)
command = input()
for i in list_numbers:
    if command == "even" and i % 2 == 0:
        filter_list.append(i)
    elif command == "odd" and i % 2 != 0:
        filter_list.append(i)
    elif command == "negative" and i < 0:
        filter_list.append(i)
    elif command == "positive" and i >= 0:
        filter_list.append(i)

print(filter_list)
