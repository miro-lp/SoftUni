a = set(input().strip().split())
n = int(input())

set_b = set()
for _ in range(n):
    set_b.update(set(input().strip().split()))

if len(set_b - a) == 0:
    print("True")
else:
    print("False")