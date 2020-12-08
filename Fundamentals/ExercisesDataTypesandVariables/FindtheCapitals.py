text = input()

list_of_capitals = []
for index, letter in enumerate(text):
    if 65 <= ord(letter) <= 90:
        list_of_capitals.append(index)

print(list_of_capitals)
