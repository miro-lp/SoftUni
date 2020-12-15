from collections import deque

food = int(input())
orders = deque([int(i) for i in input().split()])

print(max(orders))

while len(orders) > 0:
    if orders[0] <= food:
        food -= orders.popleft()
    else:
        print(f"Orders left: {' '.join([str(i) for i in orders])}")
        break

if len(orders) == 0:
    print("Orders complete")
