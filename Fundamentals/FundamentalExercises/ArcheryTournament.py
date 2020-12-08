field = [int(i) for i in input().split("|")]
points = 0
while True:
    line = input()
    if line == "Game over":
        break
    elif line == "Reverse":
        field = list(reversed(field))
    else:
        command = line.split("@")
        index = int(command[1])
        length = int(command[2])
        if command[0] == "Shoot Left":
            if index > len(field) - 1 or index < 0:
                continue
            else:
                counter = 0
                while counter < length:
                    counter += 1
                    index -= 1
                    if index < 0:
                        index = len(field) - 1
                if field[index] >= 5:
                    field[index] -= 5
                    points += 5
                elif 0 <= field[index] < 5:
                    points += field[index]
                    field[index] = 0
        elif command[0] == "Shoot Right":
            if index > len(field) - 1 or index < 0:
                continue
            else:
                counter = 0
                while counter < length:
                    counter += 1
                    index += 1
                    if index > len(field) - 1:
                        index = 0
                if field[index] >= 5:
                    field[index] -= 5
                    points += 5
                elif 0 <= field[index] < 5:
                    points += field[index]
                    field[index] = 0

field = [str(i) for i in field]
print(" - ".join(field))
print(f"Iskren finished the archery tournament with {points} points!")
