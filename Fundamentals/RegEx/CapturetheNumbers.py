import re
all_text = ""
while True:
    text = input()
    all_text += text
    if not text:
        break

pattern = r'(\d+)'
matches = re.findall(pattern, all_text)

print(' '.join(matches))

