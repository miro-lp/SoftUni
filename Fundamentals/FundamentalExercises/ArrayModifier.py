numbers = list(map(int, input().split(" ")))

while True:
    command = input()
    if command == "end":
        break
    toknes = command.split(" ")
    if toknes[0] == "swap":
        numbers[int(toknes[1])], numbers[int(toknes[2])] = numbers[int(toknes[2])], numbers[int(toknes[1])]
    elif toknes[0] == "multiply":
        num = numbers[int(toknes[1])] * numbers[int(toknes[2])]
        numbers[int(toknes[1])] = num
    elif toknes[0] == "decrease":
        numbers = [i - 1 for i in numbers]

numbers = [str(i) for i in numbers]

print(", ".join(numbers))
