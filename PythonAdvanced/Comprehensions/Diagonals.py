matrix = [[int(i) for i in input().split(", ")] for _ in range(int(input()))]

first_d = [matrix[i][j] for i in range(len(matrix)) for j in range(len(matrix[i])) if i == j]
second_d = [matrix[i][j] for i in range(len(matrix)) for j in range(len(matrix[i])) if len(matrix[i]) - 1 - i == j]
print(f"First diagonal: {', '.join(map(str, first_d))}. Sum: {sum(first_d)}")
print(f"Second diagonal: {', '.join(map(str, second_d))}. Sum: {sum(second_d)}")
