text = input()

counter = 0
strength = 0

while counter < len(text):
    bomb = text[counter]
    if bomb == ">":
        strength += int(text[counter + 1])
        if strength > 0:
            text = text[:counter + 1] + text[counter + 2:]
            strength -= 1
    else:
        if strength > 0:
            text = text[:counter] + text[counter + 1:]
            strength -= 1
            counter -= 1
    counter += 1
    
print(text)
