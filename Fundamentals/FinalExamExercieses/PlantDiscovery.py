n = int(input())

plants = {}
for i in range(n):
    line = input().split("<->")
    plants[line[0]] = [int(line[1])]
while True:
    token = input()
    if token == "Exhibition":
        break
    command = token.split(": ")[0]
    if command == "Rate" or command == "Update":
        plant, rate = token.split(": ")[1].split(" - ")
        if plant in plants:
            if command == "Rate":
                plants[plant].append(int(rate))
            elif command == "Update":
                plants[plant][0] = int(rate)
        else:
            print("error")
    elif command == "Reset":
        plant = token.split(": ")[1]
        if plant in plants:
            plants[plant] = plants[plant][:1]
        else:
            print("error")

final_plants = {}
for i in plants:
    if len(plants[i]) > 1:
        final_plants[i] = [plants[i][0], sum(plants[i][1:]) / len(plants[i][1:])]
    else:
        final_plants[i] = [plants[i][0], 0]

final_plants = dict(sorted(final_plants.items(), key=lambda x: (-x[1][0], -x[1][1])))

print("Plants for the exhibition:")
for pl in final_plants:
    print(f"- {pl}; Rarity: {final_plants[pl][0]}; Rating: {final_plants[pl][1]:.2f}")
