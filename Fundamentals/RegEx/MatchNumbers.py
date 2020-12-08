import re

text = input()

pattern = r"(^|(?<=\s))(-?\d+(\.\d+)?)($|(?=\s))"

matches = re.findall(pattern, text)

for i in matches:
    _, num, _, _ = i
    print(num, end=" ")
