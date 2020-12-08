text = input()

for index, symbol in enumerate(text):
    if symbol == ":" and text[index + 1] != " ":
        print(text[index] + text[index + 1])
