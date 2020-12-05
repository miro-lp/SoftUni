all_courses = {}

while True:
    command = input()
    if command == "end":
        break
    courses_list = command.split(" : ")
    if courses_list[0] not in all_courses:
        all_courses[courses_list[0]] = []
    all_courses[courses_list[0]].append(courses_list[1])
all_courses = dict(sorted(all_courses.items(), key=lambda x: -len(x[1])))

for course in all_courses:
    print(f"{course}: {len(all_courses[course])}")
    sorted_name = sorted(all_courses[course])
    for name in sorted_name:
        print(f"-- {name}")
