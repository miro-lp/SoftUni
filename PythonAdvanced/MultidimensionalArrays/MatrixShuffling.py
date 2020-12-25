n, m = [int(i) for i in input().split()]
matrix = [input().split() for _ in range(n)]

while True:
    line = input()
    if line == "END":
        break
    cmnd = line.split()
    if len(cmnd) == 5 and cmnd[0] == "swap" and int(cmnd[1]) < n and int(cmnd[3]) < n and int(
        cmnd[2]) < m and int(cmnd[4]) < m:
        num_1 = matrix[int(cmnd[1])][int(cmnd[2])]
        num_2 = matrix[int(cmnd[3])][int(cmnd[4])]
        matrix[int(cmnd[1])][int(cmnd[2])] = num_2
        matrix[int(cmnd[3])][int(cmnd[4])] = num_1
        print("\n".join([" ".join(map(str, row)) for row in matrix]))
    else:
        print("Invalid input!")
