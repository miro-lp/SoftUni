n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
bombs = [[int(j) for j in i.split(",")] for i in input().split()]
bomb_radios = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]

for b in bombs:
    if matrix[b[0]][b[1]] > 0:
        bomb_power = matrix[b[0]][b[1]]
        for c_x, c_y in bomb_radios:
            if 0 <= c_x + b[0] < n and 0 <= c_y + b[1] < n and matrix[c_x + b[0]][c_y + b[1]] > 0:
                matrix[c_x + b[0]][c_y + b[1]] -= bomb_power

count_cells = 0
sum_cells = 0
for row in matrix:
    for cell in row:
        if cell > 0:
            count_cells += 1
            sum_cells += cell

print(f"Alive cells: {count_cells}")
print(f"Sum: {sum_cells}")
print("\n".join([" ".join(map(str,row)) for row in matrix]))