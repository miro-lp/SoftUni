targets = [int(i) for i in input().split()]

count_shots = 0
while True:
    command = input()
    if command == "End":
        break
    index = int(command)
    if index < len(targets) and targets[index] != -1:
        count_shots += 1
        last_target = targets[index]
        targets[index] = -1
        for x, i in enumerate(targets):
            if i <= last_target and i != -1:
                i += last_target
                targets[x] = i
            elif i > last_target and i != -1:
                i -= last_target
                targets[x] = i
    else:
        continue

print(f"Shot targets: {count_shots}", end=" -> ")

for i in targets:
    print(i, end=" ")
