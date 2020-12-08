import re

text = input()

threshold = 1

patern_digits = r'(\d)'
digits = re.findall(patern_digits, text)

for i in digits:
    threshold *= int(i)
pattern_emoji = r"(:{2}|\*{2})([A-Z][a-z][a-z]+)\1"
emojis = re.findall(pattern_emoji, text)

cool_emojis = []
for i in emojis:
    total_points = 0
    _, emoji = i
    for l in emoji:
        total_points += ord(l)
    if total_points >= threshold:
        cool_emojis.append(_)
        cool_emojis.append(emoji)
        cool_emojis.append(_)

print(f"Cool threshold: {threshold}")
print(f"{len(emojis)} emojis found in the text. The cool ones are:")
for i in range(1, len(cool_emojis), 3):
    print(f"{cool_emojis[i - 1]}{cool_emojis[i]}{cool_emojis[i + 1]}")
