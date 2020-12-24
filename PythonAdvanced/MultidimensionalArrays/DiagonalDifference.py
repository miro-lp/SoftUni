n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]

prime_d = 0
second_d = 0

for i in range(len(matrix)):
    prime_d+=matrix[i][i]
    second_d+=matrix[i][len(matrix) - 1 - i]

print(abs(prime_d - second_d))