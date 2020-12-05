force_book = {}

while True:
    command = input()
    if command == "Lumpawaroo":
        break
    if " | " in command:
        line_user = command.split(" | ")
        if line_user[1] not in force_book:
            force_book[line_user[1]] = line_user[0]
    elif " -> " in command:
        line_side = command.split(" -> ")
        force_book[line_side[0]] = line_side[1]
        print(f"{line_side[0]} joins the {line_side[1]} side!")

new_force_book = {}

for i in force_book:
    if force_book[i] not in new_force_book:
        new_force_book[force_book[i]] = []
    new_force_book[force_book[i]].append(i)

new_force_book = dict(sorted(new_force_book.items(), key=lambda y: (-len(y[1]), y[0])))

for i in new_force_book:
    new_force_book[i] = sorted(new_force_book[i])

for i in new_force_book:
    if len(new_force_book[i]) != 0:
        print(f"Side: {i}, Members: {len(new_force_book[i])}")
        for j in new_force_book[i]:
            print(f"! {j}")
