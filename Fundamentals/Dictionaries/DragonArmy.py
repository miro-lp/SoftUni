n = int(input())

dragons = {}

for i in range(n):
    type, name, damage, health, armor = input().split()
    if damage == "null":
        damage = 45
    if health == "null":
        health = 250
    if armor == "null":
        armor = 10
    if type not in dragons:
        dragons[type] = {name: [int(damage), int(health), int(armor)]}
    else:
        dragons[type][name] = [int(damage), int(health), int(armor)]

type_avarage_stats = {}

for t in dragons:
    counter = 0
    dam_avr = 0
    health_avr = 0
    armor_avr = 0
    for k in dragons[t]:
        dam_avr += dragons[t][k][0]
        health_avr += dragons[t][k][1]
        armor_avr += dragons[t][k][2]
        counter += 1
    type_avarage_stats[t] = [dam_avr / counter, health_avr / counter, armor_avr / counter]
for clr in dragons:
    dragons[clr] = dict(sorted(dragons[clr].items(), key=lambda x:x[0]))

for j in dragons:
    print(f"{j}::({type_avarage_stats[j][0]:.2f}/{type_avarage_stats[j][1]:.2f}/{type_avarage_stats[j][2]:.2f})")
    for i in dragons[j]:
        print(f"-{i} -> damage: {dragons[j][i][0]}, health: {dragons[j][i][1]}, armor: {dragons[j][i][2]}")