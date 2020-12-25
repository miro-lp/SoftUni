n, m = [int(i) for i in input().split()]
snake = input()

matrix = [["" for i in range(m)] for _ in range(n)]

index = 0
for i in range(n):
    if i % 2 == 0:
        for j in range(m):
            if index == len(snake):
                index = 0
            matrix[i][j] = snake[index - len(snake)]
            index += 1
    else:
        for j in range(m - 1, -1, -1):
            if index == len(snake):
                index = 0
            matrix[i][j] = snake[index - len(snake)]
            index += 1

print("\n".join(["".join(row) for row in matrix]))
