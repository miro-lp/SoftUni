from itertools import chain

n, m = [int(i) for i in input().split()]
matrix = [[int(i) for i in input().split()] for _ in range(n)]

max_sum = -999999999999
max_square = []
for i in range(n - 2):
    for j in range(m - 2):
        square = [matrix[i][j:j + 3], matrix[i + 1][j:j + 3], matrix[i + 2][j:j + 3]]
        sum_current = sum(chain(*square))
        if sum_current > max_sum:
            max_sum = sum_current
            max_square = square

print(f"Sum = {max_sum}")
print("\n".join([" ".join(map(str,row)) for row in max_square]))
