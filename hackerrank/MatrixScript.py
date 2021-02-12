import re

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = list(input())
    matrix.append(matrix_item)

text =""
pattern = r"(?<=[A-Xa-z0-9])([!,@,#,$,%,& ]+)(?=[A-Xa-z0-9])"

for i in range(m):
    for j in range(n):
        text += matrix[j][i]

matches = re.sub(pattern," ",text)
print(matches)
