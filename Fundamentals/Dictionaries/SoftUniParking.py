n = int(input())

parked_register = {}

for i in range(n):
    command = input().split(" ")
    if command[0] == "register":
        if command[1] not in parked_register:
            parked_register[command[1]] = command[2]
            print(f"{command[1]} registered {command[2]} successfully")
        else:
            print(f"ERROR: already registered with plate number {parked_register[command[1]]}")
    else:
        if command[1] not in parked_register:
            print(f"ERROR: user {command[1]} not found")
        else:
            parked_register.pop(command[1])
            print(f"{command[1]} unregistered successfully")

for i in parked_register:
    print(f"{i} => {parked_register[i]}")
