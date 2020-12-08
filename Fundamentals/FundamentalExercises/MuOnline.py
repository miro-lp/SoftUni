health = 100
bitcoins = 0
dungeons_rooms = input().split("|")

is_all_room = True

for index, i in enumerate(dungeons_rooms):
    token = i.split()
    command = token[0]
    num = int(token[1])
    if command == "potion":
        health += num
        if health > 100:
            print(f"You healed for {100 - (health - num)} hp.")
            health = 100
        else:
            print(f"You healed for {num} hp.")
        print(f"Current health: {health} hp.")
    elif command == "chest":
        bitcoins += num
        print(f"You found {num} bitcoins.")
    else:
        health -= num
        if health > 0:
            print(f"You slayed {command}.")
        else:
            is_all_room = False
            print(f"You died! Killed by {command}.")
            print(f"Best room: {index + 1}")
            break

if is_all_room:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
