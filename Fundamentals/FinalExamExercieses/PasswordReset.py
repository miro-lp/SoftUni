text = input()

while True:
    line = input()
    if line == "Done":
        break
    command = line.split()[0]
    if command == "TakeOdd":
        new_text = ""
        for i in range(len(text)):
            if i % 2 == 1:
                new_text += text[i]
        print(new_text)
        text = new_text
    elif command == "Cut":
        index = int(line.split()[1])
        length = int(line.split()[2])
        text = text[:index] + text[index + length:]
        print(text)
    elif command == "Substitute":
        substring = line.split()[1]
        substitute = line.split()[2]
        if substring not in text:
            print("Nothing to replace!")
        else:
            text = text.replace(substring, substitute)
            print(text)

print(f"Your password is: {text}")
