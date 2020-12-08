text = input()

new_text = ""
last_letter = ""

for i in text:
    counter = 0
    if last_letter != i or last_letter == "":
        for j in text:
            if i != j:
                new_text += i
                break
            counter += 1
    last_letter = i
    text = text.replace(i, "", counter)
if len(text) == 0:
    new_text += last_letter

print(new_text)
