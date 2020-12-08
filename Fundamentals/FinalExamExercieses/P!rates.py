cities = {}

while True:
    line = input()
    if line == "Sail":
        break
    city = line.split("||")[0]
    if city not in cities:
        cities[city] = [int(line.split("||")[1]), int(line.split("||")[2])]
    else:
        cities[city][0] += int(line.split("||")[1])
        cities[city][1] += int(line.split("||")[2])
while True:
    command = input()
    if command == "End":
        break
    town = command.split("=>")[1]
    if command.split("=>")[0] == "Plunder":
        people = int(command.split("=>")[2])
        gold = int(command.split("=>")[3])
        cities[town][0] -= people
        cities[town][1] -= gold
        if cities[town][0] <= 0 or cities[town][1] <= 0:
            cities.pop(town)
            print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
            print(f"{town} has been wiped off the map!")
        else:
            print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
    elif command.split("=>")[0] == "Prosper":
        gold = int(command.split("=>")[2])
        if gold < 0:
            print(f"Gold added cannot be a negative number!")
            continue
        cities[town][1] += gold
        print(f"{gold} gold added to the city treasury. {town} now has {cities[town][1]} gold.")
cities = dict(sorted(cities.items(), key=lambda x: (-x[1][1], x[0])))

if len(cities)>0:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for i in cities:
        print(f"{i} -> Population: {cities[i][0]} citizens, Gold: {cities[i][1]} kg")
else:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")
