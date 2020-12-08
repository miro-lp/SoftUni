days = int(input())
players = int(input())
energy = float(input())
water_per_person = float(input())
food_per_person = float(input())

total_water = water_per_person * days * players
total_food = food_per_person * days * players

is_enough_energy = True
for i in range(1, days + 1):
    loss_energy = float(input())
    energy -= loss_energy
    if energy <= 0:
        print(f"You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.")
        is_enough_energy = False
        break
    if i % 2 == 0:
        total_water *= .7
        energy *= 1.05
    if i % 3 == 0:
        if players > 0:
            total_food -= (total_food / players)
        energy *= 1.1

if is_enough_energy:
    print(f"You are ready for the quest. You will be left with - {energy:.2f} energy!")
