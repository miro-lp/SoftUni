numbers = input().split(", ")
beggar_count = int(input())

numbers_list = []

for i in numbers:
    numbers_list.append(int(i))

beggar_list = []

for j in range(beggar_count):
    beggar_list.append(0)

index = 0

for k in numbers_list:
    beggar_list[index] += k
    index += 1
    if index == beggar_count:
        index = 0
print(beggar_list)
