string = input()
n = int(input())
field = [list(input()) for _ in range(n)]
m = int(input())
commands = [input() for _ in range(m)]

moves = {"up": [-1, 0],
         "down": [1, 0],
         "left": [0, -1],
         "right": [0, 1]}
coord_p = []
for i in range(n):
    for j in range(n):
        if field[i][j] == "P":
            coord_p = [i, j]
x, y = coord_p
for k in commands:
    field[x][y] = "-"
    x += moves[k][0]
    y += moves[k][1]
    if 0 <= x < n and 0 <= y < n:
        if field[x][y] != "-":
            string += field[x][y]
        field[x][y] = "P"
    else:
        if len(string) > 0:
            string = string[:-1]
        x -= moves[k][0]
        y -= moves[k][1]
        field[x][y] = "P"

print(string)
print(*["".join(row) for row in field],sep="\n")
