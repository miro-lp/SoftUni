n = int(input())
p = int(input())

res = n
for i in range(3):
    mask = (1 << (p + i))
    res = res ^ mask

print(res)
