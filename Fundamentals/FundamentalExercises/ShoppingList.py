grocery_list = input().split("!")

while True:
    line = input()
    if line == "Go Shopping!":
        break
    token = line.split()
    command = token[0]
    item = token[1]
    if command == "Urgent":
        if item in grocery_list:
            continue
        else:
            grocery_list.insert(0, item)
    elif command == "Unnecessary":
        if item in grocery_list:
            grocery_list.remove(item)
    elif command == "Correct":
        if item in grocery_list:
            for index, el in enumerate(grocery_list):
                if el == item:
                    grocery_list[index] = token[2]
    elif command == "Rearrange":
        if item in grocery_list:
            for index, el in enumerate(grocery_list):
                if el == item:
                    el_new = grocery_list.pop(index)
                    grocery_list.append(el_new)
print(", ".join(grocery_list))
