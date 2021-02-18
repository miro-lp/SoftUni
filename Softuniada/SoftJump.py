from collections import deque


def jump_p(coord, field):
    x, y = coord
    jump = 0
    is_win = False
    if 0 <= x - 1 < len(field):
        if field[x - 1][y] == "-":
            field[x - 1][y] = "S"
            jump = 1
            if x == len(field) - 1:
                field[x][y] = "0"
            else:
                field[x][y] = "-"
            coord = [x - 1, y]
    if x - 1 == 0:
        is_win = True
    return (coord, field, is_win, jump)


def rotate(field, command, coord_s):
    row, count = command
    f_row = deque(field[row])
    f_row.rotate(count)
    field[row] = list(f_row)
    if "S" in field[row]:
        y = field[row].index("S")
        coord_s = [row,y]
    return (coord_s, field)


m, n = map(int, input().split())
field = [list(input()) for _ in range(m)]
k = int(input())
commands = [list(map(int, input().split())) for _ in range(k)]

coord_s = []
for i in range(m):
    for j in range(n):
        if field[i][j] == "S":
            coord_s = [i, j]

is_win = False
count_jump = 0
for command in commands:
    coord_s, field = rotate(field, command, coord_s)
    coord_s, field, is_win, jump = jump_p(coord_s, field)
    count_jump += jump


if is_win:
    print("Win")
else:
    print("Lose")
print(f"Total Jumps: {count_jump}")
print(*["".join(row) for row in field], sep="\n")
