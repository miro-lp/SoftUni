k, n = int(input()), int(input())

arr = sorted([int(input()) for _ in range(n)])

combs = [max(arr[i:i + k]) - min(arr[i:i + k]) for i in range(len(arr) + 1 - k)]

print(min(combs))
