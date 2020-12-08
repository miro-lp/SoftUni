import re

text = input()

pattern = r"\b(\d{2})([\./-])([A-Z][a-z]{2})\2(\d{4})\b"
matches = re.findall(pattern, text)

for i in range(len(matches)):
    day, _, month, year = matches[i]
    print(f"Day: {day}, Month: {month}, Year: {year}")
