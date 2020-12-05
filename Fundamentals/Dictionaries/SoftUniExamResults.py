students = {}
courses = {}

while True:
    line = input()
    if line == "exam finished":
        break
    if len(line.split("-")) == 3:
        student, course, points = line.split("-")
    elif len(line.split("-")) == 2:
        student = line.split("-")[0]
        if student in students:
            students.pop(student)
            continue
    if student not in students:
        students[student] = int(points)
    else:
        if students[student] < int(points):
            students[student] = int(points)
    if course not in courses:
        courses[course] = 1
    else:
        courses[course] +=1


students = dict(sorted(students.items(), key=lambda x: (-x[1], x[0])))
courses = dict(sorted(courses.items(), key=lambda x: (-x[1], x[0])))

print("Results:")
for stud in students:
    print(f"{stud} | {students[stud]}")
print("Submissions:")
for crs in courses:
    print(f"{crs} - {courses[crs]}")
