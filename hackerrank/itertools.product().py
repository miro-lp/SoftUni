from itertools import product

a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

print(*list(product(a,b)))