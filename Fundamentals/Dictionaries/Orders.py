ordered_stuff = {}

while True:
    command = input()
    if command == "buy":
        break
    products = command.split(" ")
    if products[0] not in ordered_stuff:
        ordered_stuff[products[0]] = []
        ordered_stuff[products[0]].append(float(products[1]))
        ordered_stuff[products[0]].append(int(products[2]))
    else:
        ordered_stuff[products[0]][0] = float(products[1])
        ordered_stuff[products[0]][1] += int(products[2])


for i in ordered_stuff:
    print(f"{i} -> {ordered_stuff[i][0]*ordered_stuff[i][1]:.2f}")
