def same_name(word):
    new_list = []
    for index, elem in enumerate(word):
        if word[index] in word.pop(index):
            new_list.append(elem)


name_list = []
food_list = []
area_list = []

feed_name = []
feed_food = []
feed_area = []

is_same_animal = False
while True:
    command = input()
    if command == "Last Info":
        break
    list_command = command.split(":")
    if list_command[0] == "Add":
        name_list.append(list_command[1])
        food_list.append(int(list_command[2]))
        area_list.append(list_command[3])
    elif list_command[0] == "Feed":
        feed_name.append(list_command[1])
        feed_food.append(int(list_command[2]))
        feed_area.append(list_command[3])

for i in range(len(name_list)):
    len_of_list = len(name_list)
    for j in range(len_of_list - 1, 1, -1):
        if name_list[i] == name_list[j] and i != j:
            name_list.pop(j)
            food_list[i] += food_list[j]
            food_list.pop(j)
            area_list.pop(j)
    if len(set(name_list)) == len(name_list):
        break
# for i in range(len(feed_name)):
#     if feed_name[i] in name_list:
#         food_list[i] -= feed_food[i]

print(name_list)
print(food_list)
print(area_list)
