energy = int(input())
count_battles = 0
is_enough_energy = True
while True:
    command = input()
    if command == "End of battle":
        break
    line = int(command)
    if energy >= line:
        energy -= line
        count_battles += 1
        if count_battles % 3 == 0:
            energy += count_battles
    else:
        print(f"Not enough energy! Game ends with {count_battles} won battles and {energy} energy")
        is_enough_energy =False
        break

if is_enough_energy:
    print(f"Won battles: {count_battles}. Energy left: {energy}")
