n = int(input())

heroes = {}
for i in range(n):
    line = input().split()
    name = line[0]
    points = [int(i) for i in line[1:]]
    heroes[name] = points

while True:
    token = input()
    if token == "End":
        break
    command = token.split(" - ")[0]
    hero_name = token.split(" - ")[1]
    if command == "CastSpell":
        mp_needed = int(token.split(" - ")[2])
        spell_name = token.split(" - ")[3]
        if mp_needed <= heroes[hero_name][1]:
            heroes[hero_name][1] -= mp_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name][1]} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    elif command == "TakeDamage":
        damage = int(token.split(" - ")[2])
        attacker = token.split(" - ")[3]
        heroes[hero_name][0] -= damage
        if heroes[hero_name][0] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name][0]} HP left!")
        else:
            print(f"{hero_name} has been killed by {attacker}!")
            heroes.pop(hero_name)
    elif command == "Recharge":
        amount = int(token.split(" - ")[2])
        heroes[hero_name][1] += amount
        if heroes[hero_name][1] <= 200:
            print(f"{hero_name} recharged for {amount} MP!")
        elif heroes[hero_name][1] > 200:
            print(f"{hero_name} recharged for {amount - (heroes[hero_name][1] - 200)} MP!")
            heroes[hero_name][1] = 200
    elif command == "Heal":
        amount = int(token.split(" - ")[2])
        heroes[hero_name][0] += amount
        if heroes[hero_name][0] <= 100:
            print(f"{hero_name} healed for {amount} HP!")
        elif heroes[hero_name][0] > 100:
            print(f"{hero_name} healed for {amount - (heroes[hero_name][0] - 100)} HP!")
            heroes[hero_name][0] = 100

heroes = dict(sorted(heroes.items(), key=lambda x: (-x[1][0], x[0])))

for i in heroes:
    print(f"{i}")
    print(f"  HP: {heroes[i][0]}")
    print(f"  MP: {heroes[i][1]}")
