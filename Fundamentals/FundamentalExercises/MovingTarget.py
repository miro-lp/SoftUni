targets = [int(i) for i in input().split()]

while True:
    command = input()
    if command == "End":
        targets = [str(i) for i in targets]
        print("|".join(targets))
        break
    token = command.split()
    index = int(token[1])
    value = int(token[2])
    if token[0] == "Shoot":
        if 0 <= index < len(targets):
            targets[index] -= value
            if targets[index] <= 0:
                targets.pop(index)
    elif token[0] == "Add":
        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print("Invalid placement!")
    elif token[0] == "Strike":
        if index - value >= 0 and index + value < len(targets):
            targets = [n for i, n in enumerate(targets) if
                       not index - value <= i <= index + value]
        else:
            print("Strike missed!")


