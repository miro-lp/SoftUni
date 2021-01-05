import os

while True:
    line = input()
    if line == "End":
        break
    command, *args = line.split("-")
    if command == "Create":
        f = open(args[0], "w")
        f.write("")
        f.close()
    elif command == "Add":
        f = open(args[0], "a")
        f.write(f"{args[1]} \n")
        f.close()
    elif command == "Replace":
        try:
            with open(args[0], "r") as f:
                text = [i.strip() for i in f.readlines()]
            with open(args[0], "w") as f:
                for line in text:
                    if args[1] in line:
                        new_line = line.replace(args[1], args[2])
                        print(f"{new_line}", file=f)
                    else:
                        print(line, file=f)
        except FileNotFoundError:
            print("An error occurred")
    elif command == "Delete":
        try:
            os.remove(args[0])
        except FileNotFoundError:
            print("An error occurred")
