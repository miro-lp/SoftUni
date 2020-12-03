text = list(input())

list_digits = [int(i) for i in text if str(i).isdigit()]
non_numbers = [i for i in text if not str(i).isdigit()]
take_list = [i for index, i in enumerate(list_digits) if index % 2 == 0]
skip_list = [i for index, i in enumerate(list_digits) if index % 2 != 0]

final_message = []

for i in range(len(take_list)):
    for j in range(take_list[i]):
        final_message.append(non_numbers[0])
        non_numbers.pop(0)
        if len(non_numbers) == 0:
            break
    if len(non_numbers) == 0:
        break
    for k in range(skip_list[i]):
        index = 0
        non_numbers.pop(index)
        if len(non_numbers) == 0:
            break

print("".join(final_message))
