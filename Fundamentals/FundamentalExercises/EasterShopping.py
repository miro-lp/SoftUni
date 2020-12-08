shops_list = input().split()
n = int(input())

for i in range(n):
    line = input().split()
    command = line[0]
    shop = line[1]
    if len(line) > 2:
        number = int(line[2])
    if command == "Include":
        shops_list.append(shop)
    elif command == "Visit":
        if shop == "first":
            if number < len(shops_list):
                shops_list = shops_list[number:]
            elif number == len(shops_list):
                shops_list = []
        elif shop == "last":
            if number < len(shops_list):
                shops_list = shops_list[:len(shops_list) - number]
            elif number == len(shops_list):
                shops_list = []
    elif command == "Prefer":
        index = int(shop)
        if 0 <= index < len(shops_list) and 0 <= number < len(shops_list) and index != number:
            shops_list[index], shops_list[number] = shops_list[number], shops_list[index]
    elif command == "Place":
        if 0 <= number + 1 < len(shops_list):
            shops_list.insert(number + 1, shop)

print("Shops left:")
print(" ".join(shops_list))
