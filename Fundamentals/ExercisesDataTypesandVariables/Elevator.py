people = int(input())
capacity = int(input())

courses = 0

if capacity >= people:
    courses = 1
else:
    courses = people // capacity
    if people - courses * capacity != 0:
        courses += 1

print(courses)
