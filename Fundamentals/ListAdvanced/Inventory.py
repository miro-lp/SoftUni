inventory = input().split(", ")

while True:
    command = input()
    if command == "Craft!":
        break
    token = command.split(" - ")
    line = token[0]
    item = token[1]
    if line == "Collect":
        if item not in inventory:
            inventory.append(item)
    elif line == "Drop":
        if item in inventory:
            inventory.remove(item)
    elif line == "Combine Items":
        old_new_item = item.split(":")
        if old_new_item[0] in inventory:
            index = inventory.index(old_new_item[0])
            inventory.insert(index + 1, old_new_item[1])
    elif line == "Renew":
        if item in inventory:
            inventory.remove(item)
            inventory.append(item)

print(", ".join(inventory))

