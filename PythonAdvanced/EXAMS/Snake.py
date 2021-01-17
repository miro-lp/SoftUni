field = [list(input()) for _ in range(int(input()))]

moves = {"left": (0, -1), "right": (0, 1), "down": (1, 0), "up": (-1, 0)}
snake_coord = []
b_b_coord = []

for i in range(len(field)):
    for j in range(len(field[i])):
        if field[i][j] == "S":
            snake_coord = [i, j]
        elif field[i][j] == "B":
            b_b_coord.append([i, j])

food = 0

while True:
    i, j = moves[input().strip()]
    field[snake_coord[0]][snake_coord[1]] = "."
    snake_coord[0] += i
    snake_coord[1] += j
    if 0 <= snake_coord[0] < len(field) and 0 <= snake_coord[1] < len(field):
        if field[snake_coord[0]][snake_coord[1]] == "*":
            field[snake_coord[0]][snake_coord[1]] = "S"
            food += 1
            if food >= 10:
                print("You won! You fed the snake.")
                break
        elif field[snake_coord[0]][snake_coord[1]] == "B":
            field[snake_coord[0]][snake_coord[1]] = "."
            b_b_coord.remove(snake_coord)
            snake_coord = b_b_coord[0]
    else:
        print("Game over!")
        break

print(f"Food eaten: {food}")
print(*["".join(row) for row in field], sep="\n")
