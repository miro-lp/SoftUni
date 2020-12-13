text = input()

while True:
    line = input()
    if line == "Decode":
        break
    command, *others = line.split("|")
    if command == "Move":
        text = text[int(others[0]):]+ text[:int(others[0])]
    elif command == "Insert":
        text = text[:int(others[0])] + others[1] + text[int(others[0]):]
    elif command == "ChangeAll":
        text = text.replace(others[0], others[1])

print(f"The decrypted message is: {text}")
