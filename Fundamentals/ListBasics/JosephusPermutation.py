numbers_list = input().split(" ")
killer_num = int(input())

permutated_list = []

counter = 0
index = 0

while len(numbers_list) > 0:
    counter += 1
    if counter % killer_num == 0:
        permutated_list.append(int(numbers_list.pop(index)))
    else:
        index += 1
    if index >= len(numbers_list):
        index = 0


print(str(permutated_list).replace(" ",""))
