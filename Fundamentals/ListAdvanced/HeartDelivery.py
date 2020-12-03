places = [int(i) for i in input().split("@")]

command = input()
index = 0
last_place = 0
while command != "Love!":
    jump_length = int(command.split()[1])
    index += jump_length
    if index > len(places) - 1:
        index = 0
    places[index] -= 2
    if places[index] == -2:
        print(f"Place {index} already had Valentine's day.")
        places[index] = 0
    elif places[index] == 0:
        print(f"Place {index} has Valentine's day.")
    last_place = index
    command = input()

failed_places = [i for i in places if i != 0]

print(f"Cupid's last position was {last_place}.")
if len(failed_places)>0:
    print(f"Cupid has failed {len(failed_places)} places.")
else:
    print("Mission was successful.")
