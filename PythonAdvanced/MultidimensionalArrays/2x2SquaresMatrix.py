n, m = [int(i) for i in input().split()]
matrix = [input().split() for _ in range(n)]

squares = []
for i in range(len(matrix) - 1):
    for j in range(len(matrix[i]) - 1):
        square = matrix[i][j] + matrix[i][j + 1] + matrix[i + 1][j] + matrix[i + 1][j + 1]
        if square.count(square[0])==len(square):
            squares.append(square)

print(len(squares))
