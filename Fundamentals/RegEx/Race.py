import re

names = {i.split()[0]: 0 for i in input().split(",")}

pattern = r"([A-Z]|[a-z]|\d)"
while True:
    data = input()
    name = ""
    distance = 0
    if data == "end of race":
        break
    matches = re.findall(pattern, data)
    for i in matches:
        if str(i).isdigit():
            distance += int(i)
        else:
            name += i
    if name in names:
        names[name] += distance

names = dict(sorted(names.items(), key=lambda x: -x[1]))

for index, name in enumerate(names):
    if index == 0:
        print(f"{index + 1}st place: {name}")
    elif index == 1:
        print(f"{index + 1}nd place: {name}")
    elif index == 2:
        print(f"{index + 1}rd place: {name}")
