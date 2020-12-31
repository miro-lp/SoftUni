def displayPathtoPrincess(n, grid):
    coord_p = None
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "p":
                coord_p = (i, j)
                break
    coord_m = ((n - 1) // 2, (n - 1) // 2)
    yy = coord_m[0] - coord_p[0]
    xx = coord_m[1] - coord_p[1]
    if yy > 0:
        print("UP" + (yy - 1) * ("\n" + "UP"))
    elif yy < 0:
        print("DOWN" + (abs(yy) - 1) * ("\n" + "DOWN"))
    if xx > 0:
        print("LEFT" + (xx - 1) * ("\n" + "LEFT"))
    elif xx < 0:
        print("RIGHT" + (abs(xx) - 1) * ("\n" + "RIGHT"))


# print all the moves here

m = int(input())
grid = []
for i in range(0, m):
    grid.append(input().strip())

displayPathtoPrincess(m, grid)
