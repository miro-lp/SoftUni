text = [i.split("-") for i in input().split("|")]

energy = 100
coins = 100
is_bankrupt = False
for item in text:
    event = item[0]
    num_event = int(item[1])
    if event == "rest":
        energy += num_event
        if energy > 100:
            energy = 100
            print(f"You gained 0 energy.")
        else:
            print(f"You gained {num_event} energy.")
        print(f"Current energy: {energy}.")
    elif event == "order":
        if energy >= 30:
            energy -= 30
            coins += num_event
            print(f"You earned {num_event} coins.")
        else:
            energy += 50
            print(f"You had to rest!")
    else:
        if coins > num_event:
            coins -= num_event
            print(f"You bought {event}.")
        else:
            print(f"Closed! Cannot afford {event}.")
            is_bankrupt = True
            break
if not is_bankrupt:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
