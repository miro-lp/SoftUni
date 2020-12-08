text = input()

while True:
    line = input()
    if line == "Travel":
        break
    command = line.split(":")[0]
    index = line.split(":")[1]
    string = line.split(":")[2]
    if command == "Add Stop":
        index = int(index)
        if 0 <= index < len(text):
            text = text[:index] + string + text[index:]
        print(text)
    elif command == "Remove Stop":
        index = int(index)
        string = int(string)
        if 0 <= index < len(text) and 0 <= string < len(text):
            text = text[:index] + text[string + 1:]
        print(text)
    elif command == "Switch":
        if index in text:
            text = text.replace(index, string)
        print(text)

print(f"Ready for world tour! Planned stops: {text}")
