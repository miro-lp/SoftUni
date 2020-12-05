players = {}

data = input()
while data != "Season end":
    if " -> " in data:
        player, position, skill = data.split(" -> ")
        if player not in players:
            players[player] = {position: int(skill)}
        else:
            if position not in players[player]:
                players[player][position] = int(skill)
            else:
                if int(skill) > players[player][position]:
                    players[player][position] = int(skill)
    elif " vs " in data:
        plr_1, plr_2 = data.split(" vs ")
        if plr_1 and plr_2 in players:
            for i in players[plr_1].keys():
                if i in players[plr_2]:
                    if players[plr_1][i] > players[plr_2][i]:
                        players.pop(plr_2)
                        break
                    elif players[plr_1][i] < players[plr_2][i]:
                        players.pop(plr_1)
                        break

    data = input()

skills = {}
for i in players.keys():
    skills[i] = 0
    for j in players[i].keys():
        skills[i] += players[i][j]
skills = dict(sorted(skills.items(), key= lambda x:(-x[1], x[0])))

for i in players:
    players[i] = dict(sorted(players[i].items(), key=lambda y: (-y[1],y[0])))

for i in skills:
    print(f"{i}: {skills[i]} skill")
    for j in players[i]:
        print(f"- {j} <::> {players[i][j]}")

