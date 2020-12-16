from collections import deque

price = int(input())
size_barrel = int(input())
bullets_size = [int(i) for i in input().split()]
locks_size = deque([int(i) for i in input().split()])
money = int(input())

counter = 0

while len(locks_size) > 0:
    if len(bullets_size) > 0:
        lock = locks_size[0]
        while len(bullets_size) > 0:
            bullet = bullets_size.pop()
            counter += 1
            if bullet <= lock:
                locks_size.popleft()
                print("Bang!")
                if counter % size_barrel == 0 and len(bullets_size) > 0:
                    print("Reloading!")
                break
            else:
                print("Ping!")
                if counter % size_barrel == 0 and len(bullets_size) > 0:
                    print("Reloading!")
    else:
        break

if len(locks_size) == 0:
    print(f"{len(bullets_size)} bullets left. Earned ${money - counter * price}")
else:
    print(f"Couldn't get through. Locks left: {len(locks_size)}")
