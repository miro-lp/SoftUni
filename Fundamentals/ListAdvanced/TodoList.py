notes = []

while True:
    command = input()
    if command == "End":
        break
    tokens = command.split("-", maxsplit=1)
    index = int(tokens[0])
    task = tokens[1]
    notes.append((index, task))

result = [note for index, note in sorted(notes)]


print(result)
