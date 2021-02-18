n = int(input())
field = [input().split() for _ in range(n)]

moves = {"left": (0, -1),
         "right": (0, 1),
         "down": (1, 0),
         "up": (-1, 0)}

coords_p = []

for i in range(n):
    for j in range(n):
        if field[i][j] == "P":
            coords_p = [i, j]
            break

count_coins = 0
player_moves = []
is_won = None
while True:
    command = input()
    if command in moves:
        x, y = coords_p
        x_m, y_m = moves[command]
        if 0 <= x + x_m < n and 0 <= y + y_m < n:
            if field[x + x_m][y + y_m] == "X":
                is_won = False
                count_coins *= 0.5
                break
            else:
                count_coins += int(field[x + x_m][y + y_m])
                field[x + x_m][y + y_m] = 0
                player_moves.append([x + x_m, y + y_m])
                coords_p = [x + x_m, y + y_m]
                if count_coins >= 100:
                    is_won = True
                    break
        else:
            count_coins *= 0.5
            is_won = False
            break

if is_won:
    print(f"You won! You've collected {count_coins} coins.")
else:
    print(f"Game over! You've collected {int(count_coins)} coins.")
print("Your path:")
print(*player_moves, sep="\n")
