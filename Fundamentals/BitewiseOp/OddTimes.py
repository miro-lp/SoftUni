array = [int(i) for i in input().split()]

res = 0

for i in array:
    res = i^res

print(res)