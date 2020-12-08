text = input()

while True:
    line = input()
    if line == "Generate":
        break
    command = line.split(">>>")[0]
    if command == "Contains":
        word = line.split(">>>")[1]
        if word in text:
            print(f"{text} contains {word}")
        else:
            print("Substring not found!")
    elif command == "Flip":
        strt_i = int(line.split(">>>")[2])
        end_i = int(line.split(">>>")[3])
        if line.split(">>>")[1] == "Upper":
            flip_text = text[strt_i:end_i]
            flip_text = flip_text.upper()
            text = text[:strt_i] + flip_text + text[end_i:]
            print(text)
        elif line.split(">>>")[1] == "Lower":
            flip_text = text[strt_i:end_i]
            flip_text = flip_text.lower()
            text = text[:strt_i] + flip_text + text[end_i:]
            print(text)
    elif command == "Slice":
        index_1 = int(line.split(">>>")[1])
        index_2 = int(line.split(">>>")[2])
        text = text[:index_1]+text[index_2:]
        print(text)

print(f"Your activation key is: {text}")