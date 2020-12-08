import re

text = input()

destinations = []
pattern = r"([=|/])([A-Z][A-Za-z]{2,})\1"
matches = re.findall(pattern, text)

for i in matches:
    _, place = i
    destinations.append(place)

points = 0
for pl in destinations:
    for symb in pl:
        points += 1

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {points}")
