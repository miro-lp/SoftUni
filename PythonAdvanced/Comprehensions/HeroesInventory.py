heroes = input().split(", ")
invtry = {i: {} for i in heroes}

while True:
    line = input()
    if line == "End":
        break
    hero, item, price = line.split("-")
    if item not in invtry[hero]:
        invtry[hero][item] = price

print("\n".join(
    [f"{i} -> Items: {len(invtry[i])}, Cost: {sum([int(invtry[i][j]) for j in invtry[i]])}" for i in invtry]))
