board = [input().split() for _ in range(8)]

coord_k = []
for i in range(8):
    for j in range(8):
        if board[i][j] == "K":
            coord_k = [i, j]
            break
moves = {"hor_l": [0, -1], "hor_r": [0, 1],
         "ver_u": [-1, 0], "ver_d": [1, 0],
         "diag_l_u": [-1, -1], "diag_l_d": [1, -1],
         "diag_r_u": [-1, 1], "diag_r_d": [1, 1]}

coord_q = []
for key in moves:
    x, y = coord_k
    while True:
        x += moves[key][0]
        y += moves[key][1]
        if 0 <= x < 8 and 0 <= y < 8:
            if board[x][y] == "Q":
                coord_q.append([x, y])
                break
        else:
            break

if len(coord_q) > 0:
    print(*coord_q, sep="\n")
else:
    print("The king is safe!")
