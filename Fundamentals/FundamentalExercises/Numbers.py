numbers = list(map(int, input().split(" ")))

average_num = sum(numbers) / len(numbers)

above_average_list = list(reversed(sorted([i for i in numbers if i > average_num])))

top_5_list = []

if len(above_average_list) > 0:
    i = 0
    while len(top_5_list) < 5:
        top_5_list.append(above_average_list[i])
        i += 1
        if i > len(above_average_list) - 1:
            break
else:
    print("No")

top_5_list = [str(i) for i in top_5_list]

print(" ".join(top_5_list))
