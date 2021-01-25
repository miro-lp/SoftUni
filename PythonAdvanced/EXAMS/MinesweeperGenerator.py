n = int(input())
m = int(input())

bomb_coord = [(list(map(int, input()[1:-1].split(", ")))) for _ in range(m)]

matrix = [["*" if [i, j] in bomb_coord else 0 for j in range(n)] for i in range(n)]

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 0:
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if 0 <= k + i < n and 0 <= j + l < n and matrix[i + k][j + l] == "*":
                        matrix[i][j] += 1

print(*[" ".join(map(str, row)) for row in matrix], sep="\n")
