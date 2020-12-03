text = input().split()

list_A = []
list_B = []

for i in text:
    if "A-" in i:
        list_A.append(i)
    else:
        list_B.append(i)

list_A = set(list_A)
list_B = set(list_B)

count_team_A = 11 - len(list_A)
count_team_B = 11 - len(list_B)
if count_team_A < 6:
    count_team_A = 6
if count_team_B < 6:
    count_team_B = 6
print(f"Team A - {count_team_A}; Team B - {count_team_B}")
if len(list_A) > 4 or len(list_B) > 4:
    print("Game was terminated")
