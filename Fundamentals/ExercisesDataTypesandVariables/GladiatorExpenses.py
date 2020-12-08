lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
trashed_helmet_count = 0
trashed_sword_count = 0
trashed_shield_count = 0
trashed_armor_count = 0
trashed_shield_count_varible = 0
for i in range(1, lost_fights_count + 1):
    if i % 2 == 0:
        trashed_helmet_count += 1
    if i % 3 == 0:
        trashed_sword_count += 1
    if i % 2 == 0 and i % 3 == 0:
        trashed_shield_count += 1
        trashed_shield_count_varible += 1
    if trashed_shield_count_varible % 2 == 0 and trashed_shield_count_varible != 0:
        trashed_armor_count += 1
        trashed_shield_count_varible -= 2

total_cost = trashed_helmet_count * helmet_price + trashed_sword_count * sword_price + trashed_shield_count * shield_price + trashed_armor_count * armor_price
print(f"Gladiator expenses: {total_cost:.2f} aureus")
