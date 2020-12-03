first_list = input().split(", ")
second_list = input()

result = []

for element in first_list:
    if element in second_list:
        result.append(element)

print(result)
