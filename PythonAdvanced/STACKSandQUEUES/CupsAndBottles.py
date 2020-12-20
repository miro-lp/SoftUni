from collections import deque

cups = deque([int(i) for i in input().split()])
bottles = [int(i) for i in input().split()]

water = 0

while len(cups) > 0:
    cup = cups.popleft()
    while len(bottles) > 0:
        bottle = bottles.pop()
        cup -= bottle
        if cup <= 0:
            water -= cup
            break
    if len(bottles)==0:
        break

if len(cups) > 0:
    print(f"Cups: {' '.join([str(i) for i in cups])}")
elif len(bottles) > 0:
    print(f"Bottles: {' '.join([str(i) for i in bottles])}")
print(f"Wasted litters of water: {water}")
