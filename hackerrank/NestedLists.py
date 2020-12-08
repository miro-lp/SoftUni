students = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name, score])

students = list(sorted(students, key=lambda x: (x[1], x[0])))
students = [i for i in students if i[1] > students[0][1]]
for i in students:
    if students[0][1] == i[1]:
        print(i[0])
