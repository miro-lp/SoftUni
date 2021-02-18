from collections import deque

effects = deque(map(int, input().split(", ")))
powers = list(map(int, input().split(", ")))

fireworks = {"Palm Fireworks": 0,
             "Willow Fireworks": 0,
             "Crossette Fireworks": 0,
             }

is_perfect = False
while len(effects) > 0 and len(powers) > 0 and not is_perfect:
    e_f = effects[0]
    p_f = powers[-1]
    while e_f <= 0 and len(effects) > 0:
        e_f = effects.popleft()
    while p_f <= 0 and len(powers) > 0:
        p_f = powers.pop()
    if len(effects) > 0 and len(powers) > 0:
        e_f = effects.popleft()
        p_f = powers.pop()
    else:
        break
    sum_f = e_f + p_f
    if sum_f % 3 == 0 and sum_f % 5 != 0:
        fireworks["Palm Fireworks"] += 1
    elif sum_f % 3 != 0 and sum_f % 5 == 0:
        fireworks["Willow Fireworks"] += 1
    elif sum_f % 3 == 0 and sum_f % 5 == 0:
        fireworks["Crossette Fireworks"] += 1
    else:
        e_f -= 1
        effects.append(e_f)
        powers.append(p_f)
    if fireworks["Palm Fireworks"] >= 3 and fireworks["Willow Fireworks"] >= 3 \
            and fireworks["Crossette Fireworks"] >= 3:
        is_perfect = True

if is_perfect:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can’t make the perfect firework show.")
if len(effects) > 0:
    print(f"Firework Effects left: {', '.join(map(str, effects))}")
if len(powers) > 0:
    print(f"Explosive Power left: {', '.join(map(str, powers))}")
for f_w in fireworks:
    print(f"{f_w}: {fireworks[f_w]}")
