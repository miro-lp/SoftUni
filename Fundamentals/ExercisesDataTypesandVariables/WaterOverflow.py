n = int(input())

TANK_CAPACITY = 255
capacity = 0

for i in range(n):
    quantity = int(input())
    if quantity > TANK_CAPACITY:
        print("Insufficient capacity!")
    else:
        capacity += quantity
        if capacity <= TANK_CAPACITY:
            continue
        else:
            print("Insufficient capacity!")
            capacity -= quantity
print(capacity)
