gift_list = input().split(" ")

command = input()

while command != "No Money":
    command_list = command.split(" ")
    if command_list[0] == "OutOfStock":
        for index, gift in enumerate(gift_list):
            if gift == command_list[1]:
                gift_list[index] = "None"
    elif command_list[0] == "Required":
        index = int(command_list[2])
        if 0 < index < len(gift_list):
            gift_list[index] = command_list[1]
    elif command_list[0] == "JustInCase":
        gift_list[-1] = command_list[1]
    command = input()

for left_gift in gift_list:
    if left_gift != "None":
        print(left_gift, end=" ")
