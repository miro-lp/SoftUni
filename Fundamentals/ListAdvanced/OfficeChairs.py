count_room = int(input())

chairs = []
for i in range(count_room):
    command = input().split(" ")
    chairs.append(command)

is_game_on = True
count_free_chair = 0

for index, i in enumerate(chairs):
    if len(i[0]) >= int(i[1]):
        count_free_chair += (len(i[0]) - int(i[1]))
    else:
        print(f"{int(i[1]) - len(i[0])} more chairs needed in room {index + 1}")
        is_game_on = False

if is_game_on:
    print(f"Game On, {count_free_chair} free chairs left")
