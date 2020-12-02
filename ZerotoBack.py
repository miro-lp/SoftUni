text = input().split(", ")

zero_list = []
non_zero_list = []

for num in text:
    if int(num) != 0:
        non_zero_list.append(int(num))
    elif int(num) == 0:
        zero_list.append((int(num)))

back_zero_list = []
for i in range(len(non_zero_list)):
    back_zero_list.append(non_zero_list[i])
for i in range(len(zero_list)):
    back_zero_list.append(zero_list[i])

print(back_zero_list)
