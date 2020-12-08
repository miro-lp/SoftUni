text = input().split()

line = input()
while line != "Stop":
    command = line.split()
    if command[0] == "Delete":
        index = int(command[1]) + 1
        if 0 <= index < len(text):
            text = text[:index]+text[index+1:]
    elif command[0] == "Swap":
        word_1 = command[1]
        word_2 = command[2]
        if word_2 and word_1 in text:
            index_1 = text.index(word_1)
            index_2 = text.index(word_2)
            text[index_1], text[index_2] = text[index_2], text[index_1]
    elif command[0] == "Put":
        word = command[1]
        index = int(command[2]) - 1
        if 0 <= index < len(text)-1:
            text.insert(index, word)
        elif index == len(text) - 1:
            text[index] = word
    elif command[0] == "Sort":
        text = [i.lower() for i in text]
        text = list(sorted(text, reverse=True))
    elif command[0] == "Replace":
        word_1 = command[1]
        word_2 = command[2]
        if word_2 in text:
            for i in range(len(text)):
                if text[i] == word_2:
                    text[i] = word_1
    line = input()

print(" ".join(text))
