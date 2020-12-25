n = int(input())
commands = input().split()
field = [input().split() for _ in range(n)]

moves_coord = []
for i in commands:
    if i == "up":
        moves_coord.append((-1, 0))
    elif i == "down":
        moves_coord.append((1, 0))
    elif i == "right":
        moves_coord.append((0, 1))
    elif i == "left":
        moves_coord.append((0, -1))

count_coal = 0
possition_miner = []

for i in range(len(field)):
    for j in range(len(field[i])):
        if field[i][j] == "c":
            count_coal += 1
        elif field[i][j] == "s":
            possition_miner.append((i, j))

is_game_over = False
for i, j in moves_coord:
    x, y = possition_miner[0]
    if 0 <= x + i < n and 0 <= y + j < n:
        possition_miner.pop()
        possition_miner.append((x + i, y + j))
        if field[x + i][y + j] == "c":
            count_coal -= 1
            field[x + i][y + j] = "*"
            if count_coal == 0:
                print(f"You collected all coals! ({x + i}, {y + j})")
                break
        elif field[x + i][y + j] == "e":
            print(f"Game over! ({x + i}, {y + j})")
            is_game_over = True
            break

if not is_game_over and count_coal > 0:
    print(f"{count_coal} coals left. {possition_miner[0]}")
