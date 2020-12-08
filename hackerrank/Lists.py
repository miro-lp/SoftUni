n = int(input())
list = []
for i in range(n):
    data = input().split()
    command = data[0]
    if command == "append":
        list.append(int(data[1]))
    elif command == "print":
        print(list)
    elif command == "insert":
        list.insert(int(data[1]), int(data[2]))
    elif command == "pop":
        list.pop()
    elif command == "remove":
        list.remove(int(data[1]))
    elif command == "sort":
        list.sort()
    elif command == "reverse":
        list = list[::-1]
