n = int(input())

students = {}

for i in range(n):
    name = input()
    grade = float(input())
    if name not in students:
        students[name] = []
    students[name].append(grade)

good_students = {}

for stud in students:
    average_grade = sum(students[stud]) / len(students[stud])
    if average_grade >= 4.5:
        good_students[stud] = average_grade

good_students = dict(sorted(good_students.items(), key=lambda x: -x[1]))

for i in good_students:
    print(f"{i} -> {good_students[i]:.2f}")
