from collections import deque

effects = deque(map(int, input().split(", ")))
casings = list(map(int, input().split(", ")))

bombs = {"Cherry Bombs": [60, 0],
         "Datura Bombs": [40, 0],
         "Smoke Decoy Bombs": [120, 0]
         }
is_filled = False

while len(effects) > 0 and len(casings) > 0:
    e_b = effects.popleft()
    c_b = casings.pop()
    is_found = False
    for i in range(c_b, -1, -5):
        for bomb in bombs:
            if bombs[bomb][0] == e_b + i:
                bombs[bomb][1] += 1
                is_found = True
                break
        if len([True for i in bombs if bombs[i][1]>=3])==3:
            is_filled = True
        if is_found:
            break
    if is_filled:
        break

if is_filled:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if len(effects) > 0:
    print(f"Bomb Effects: {', '.join(map(str, effects))}")
else:
    print("Bomb Effects: empty")

if len(casings) > 0:
    print(f"Bomb Casings: {', '.join(map(str, casings))}")
else:
    print("Bomb Casings: empty")

for key in bombs:
    print(f"{key}: {bombs[key][1]}")
