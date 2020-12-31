rows = int(input())
matrix = [list(map(int, input().split())) for _ in range(rows)]

while True:
    line = input()
    if line == "END":
        break
    command, row, col, value = line.split()
    if int(row) >= rows or int(row) < 0 or int(col) >= rows or int(col) < 0:
        print("Invalid coordinates")
    else:
        if command == "Add":
            matrix[int(row)][int(col)] += int(value)
        elif command == "Subtract":
            matrix[int(row)][int(col)] -= int(value)


print("\n".join([" ".join([str(j) for j in i])for i in matrix]))
