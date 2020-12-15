clothes = [int(i) for i in input().split()]
capacity = int(input())

initial_capacity = capacity

racks = 1
while len(clothes) > 0:
    if clothes[-1] <= capacity:
        capacity -= clothes.pop()
    else:
        capacity = initial_capacity
        capacity -= clothes.pop()
        racks += 1

print(racks)
