n = int(input())

stack = []

for _ in range(n):
    line = input().split()
    command = line[0]
    if command == "1":
        stack.append(int(line[1]))
    elif command == "2":
        if len(stack) > 0:
            stack.pop()
    elif command == "3":
        if len(stack) > 0:
            print(max(stack))
    elif command == "4":
        if len(stack) > 0:
            print(min(stack))

while len(stack) > 1:
    print(stack.pop(), end=", ")

if len(stack) > 0:
    print(stack.pop())
