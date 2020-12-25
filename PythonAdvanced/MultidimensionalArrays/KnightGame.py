n = int(input())
board = [list(input()) for _ in range(n)]


def k_board(board):
    knights = {}
    for i in range(n):
        for j in range(n):
            counter = 0
            if board[i][j] == "K":
                for x in [1, -1]:
                    for y in [2, -2]:
                        if 0 <= i + x < n and 0 <= j + y < n:
                            if board[i + x][j + y] == board[i][j]:
                                counter += 1
                        if 0 <= i + y < n and 0 <= j + x < n:
                            if board[i + y][j + x] == board[i][j]:
                                counter += 1
                knights[(i, j)] = counter
    knights = dict(sorted(knights.items(), key=lambda x: -x[1]))
    return knights


total_count = 0
knights_1 = k_board(board)


for i in range(len(knights_1)):
    key = list(knights_1.keys())[0]
    if knights_1[key] > 0:
        i, j = key
        total_count += 1
        board[i][j] = "0"
        knights_1 = k_board(board)
    else:
        break

print(total_count)

