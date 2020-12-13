import re

text = input()

pattern = r"([\#|\|])(?P<food>[A-Za-z\s]+)\1(?P<date>\d{2}\/\d{2}\/\d{2})\1(?P<calories>\d{1,5})\1"
matches = [i.groupdict() for i in re.finditer(pattern, text)]

days = sum([int(i["calories"]) for i in matches]) // 2000

print(f"You have food to last you for: {days} days!")
for i in matches:
    keys = i.keys()
    print(f"Item: {i['food']}, Best before: {i['date']}, Nutrition: {i['calories']}")
