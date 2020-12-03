wagons_count = int(input())

wagons = [0] * wagons_count

while True:
    command = input()
    if command == "End":
        break
    token = command.split(" ")
    if token[0] == "add":
        wagons[-1] += int(token[1])
    elif token[0] == "insert":
        index = int(token[1])
        wagons[index] += int(token[2])
    elif token[0] == "leave":
        index = int(token[1])
        wagons[index] -= int(token[2])

print(wagons)
