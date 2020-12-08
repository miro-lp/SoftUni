numbers = [int(i) for i in input().split()]

while True:
    line = input()
    if line == "END":
        break
    token = line.split()
    command = token[0]
    if len(token) > 1:
        num_1 = int(token[1])
    if len(token) > 2:
        num_2 = int(token[2])
    if command == "Change":
        if num_1 in numbers:
            index = numbers.index(num_1)
            numbers[index] = num_2
    elif command == "Hide":
        if num_1 in numbers:
            numbers.remove(num_1)
    elif command == "Switch":
        if num_1 and num_2 in numbers:
            index_1 = numbers.index(num_1)
            index_2 = numbers.index(num_2)
            numbers[index_1], numbers[index_2] = numbers[index_2], numbers[index_1]
    elif command == "Insert":
        place = num_1 + 1
        if 0 <= place < len(numbers):
            numbers.insert(place, num_2)
    elif command == "Reverse":
        numbers = numbers[::-1]

numbers = [str(j) for j in numbers]

print(" ".join(numbers))
