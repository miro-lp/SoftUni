def mutated_bunnies(matrix):
    is_reached_player = False
    bunny_coord = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "B":
                bunny_coord.append((i, j))
    for i, j in bunny_coord:
        if 0 <= i + 1 < n and matrix[i + 1][j] == ".":
            matrix[i + 1][j] = "B"
        elif 0 <= i + 1 < n and matrix[i + 1][j] == "P":
            matrix[i + 1][j] = "B"
            is_reached_player = True
        if 0 <= i - 1 < n and matrix[i - 1][j] == ".":
            matrix[i - 1][j] = "B"
        elif 0 <= i - 1 < n and matrix[i - 1][j] == "P":
            matrix[i - 1][j] = "B"
            is_reached_player = True
        if 0 <= j + 1 < m and matrix[i][j + 1] == ".":
            matrix[i][j + 1] = "B"
        elif 0 <= j + 1 < m and matrix[i][j + 1] == "P":
            matrix[i][j + 1] = "B"
            is_reached_player = True
        if 0 <= j - 1 < m and matrix[i][j - 1] == ".":
            matrix[i][j - 1] = "B"
        elif 0 <= j - 1 < m and matrix[i][j - 1] == "P":
            matrix[i][j - 1] = "B"
            is_reached_player = True
    if is_reached_player:
        return True


def moves_player(coord, matrix):
    x, y = coord
    is_won = False
    is_dead = False
    is_stopped = False
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "P":
                if 0 <= i + x < n and 0 <= j + y < m and matrix[i + x][j + y] == ".":
                    matrix[i + x][j + y] = "P"
                    matrix[i][j] = "."
                    xx = i + x
                    yy = j + y
                    is_stopped = True
                    break
                elif 0 <= i + x < n and 0 <= j + y < m and matrix[i + x][j + y] == "B":
                    matrix[i][j] = "."
                    xx = i + x
                    yy = j + y
                    is_dead = True
                    is_stopped = True
                    break
                elif -1 == i + x or i + x == n or -1 == j + y or j + y == m:
                    matrix[i][j] = "."
                    xx = i
                    yy = j
                    is_won = True
                    is_stopped = True
                    break
        if is_stopped:
            break
    return [is_won, is_dead, (xx, yy)]


n, m = [int(i) for i in input().split()]
lair = [list(input()) for _ in range(n)]
directions = list(input())

moves_coord = []
for i in directions:
    if i == "U":
        moves_coord.append((-1, 0))
    elif i == "D":
        moves_coord.append((1, 0))
    elif i == "R":
        moves_coord.append((0, 1))
    elif i == "L":
        moves_coord.append((0, -1))

is_dead_by_bunnies = False
is_won = False
is_dead = False

for move in moves_coord:
    is_won, is_dead, coord = moves_player(move, lair)
    coord_x, coord_y = coord
    is_dead_by_bunnies = mutated_bunnies(lair)
    if is_dead_by_bunnies or is_dead or is_won:
        print("\n".join(["".join(row) for row in lair]))
        if is_won:
            print(f"won: {coord_x} {coord_y}")
            break
        elif is_dead:
            print(f"dead: {coord_x} {coord_y}")
            break
        elif is_dead_by_bunnies:
            print(f"dead: {coord_x} {coord_y}")
            break
