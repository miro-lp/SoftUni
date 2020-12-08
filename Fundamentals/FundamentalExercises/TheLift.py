people = int(input())
wagons = [int(i) for i in input().split()]

first_count_people = people

new_wagons = []
for i in wagons:
    while i < 4:
        if people > 0:
            people -= 1
            i += 1
        else:
            break
    new_wagons.append(i)

new_wagons_str = [str(i) for i in new_wagons]

if people > 0:
    print(f"There isn't enough space! {people} people in a queue!")
    print(" ".join(new_wagons_str))
elif people == 0 and len(new_wagons) * 4 == sum(new_wagons):
    print(" ".join(new_wagons_str))
else:
    print(f"The lift has empty spots!")
    print(" ".join(new_wagons_str))
