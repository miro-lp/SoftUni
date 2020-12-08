import re

names = input().split(",")

pattern_health = r"([^0-9\.\-\*\/\+])"
pattern_damage = r"(-?\d+\.?\d*)"
demons = {}
for name in names:
    name = name.split()[0]
    health = 0
    damage = 0
    matches_health = re.findall(pattern_health, name)
    matches_damage = re.findall(pattern_damage, name)
    for i in matches_health:
        health += ord(i)
    for j in matches_damage:
        damage += float(j)
    for k in name:
        if k == "*":
            damage *= 2
        elif k == "/":
            damage /= 2
    demons[name] = [health, damage]

demons = dict(sorted(demons.items(), key=lambda x: x[0]))

for name in demons:
    print(f"{name} - {demons[name][0]} health, {demons[name][1]:.2f} damage")
