text = input()

while True:
    line = input()
    if line == "Reveal":
        break
    command = line.split(":|:")[0]
    if command == "InsertSpace":
        index = int(line.split(":|:")[1])
        text = text[:index] + " " + text[index:]
        print(text)
    elif command == "Reverse":
        substring = line.split(":|:")[1]
        if substring not in text:
            print("error")
        else:
            # ind = text.find(substring)
            # text = text[:ind] + text[(ind + len(substring)) + 1:] + substring[::-1]
            text = text.replace(substring,"",1) + substring[::-1]
            print(text)
    elif command == "ChangeAll":
        sbstg = line.split(":|:")[1]
        rplmnt = line.split(":|:")[2]
        text = text.replace(sbstg, rplmnt)
        print(text)

print(f"You have a new text message: {text}")