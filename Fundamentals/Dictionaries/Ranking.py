contests = {}
students = {}

while True:
    line = input()
    if line == "end of contests":
        break
    cnst, pswrd = line.split(":")
    contests[(cnst, pswrd)] = []

while True:
    sbmssn = input()
    if sbmssn == "end of submissions":
        break
    cnst, pswrd, *studs = sbmssn.split("=>")
    if (cnst, pswrd) in contests:
        if (cnst, studs[0]) not in students:
            students[(cnst, studs[0])] = int(studs[1])
        else:
            if int(studs[1]) > students[(cnst, studs[0])]:
                students[(cnst, studs[0])] = int(studs[1])
        if studs[0] in contests[(cnst, pswrd)]:
            for i in range(len(contests[(cnst, pswrd)])):
                if contests[(cnst, pswrd)][i] == studs[0] and int(contests[(cnst, pswrd)][i + 1]) < int(studs[1]):
                    contests[((cnst, pswrd))][i + 1] = studs[1]
        else:
            contests[(cnst, pswrd)].append(studs[0])
            contests[(cnst, pswrd)].append(studs[1])

total_points = {}
for i in students:
    cours, student = i
    if student in total_points:
        total_points[student] += students[i]
    else:
        total_points[student] = students[i]

students_1 = {}
for i in students:
    cours, student = i
    if student not in students_1:
        students_1[student] = []
        students_1[student].append(cours)
        students_1[student].append(students[i])
    else:
        students_1[student].append(cours)
        students_1[student].append(students[i])

name_max_point = ""
max_point = 0
for i in total_points:
    if max_point < total_points[i]:
        max_point = total_points[i]
        name_max_point = i

print(f"Best candidate is {name_max_point} with total {max_point} points.")

students = dict(sorted(students.items(), key=lambda x: (x[0][1], -x[1])))

students_1 = {}
for i in students:
    cours, student = i
    if student not in students_1:
        students_1[student] = []
        students_1[student].append(cours)
        students_1[student].append(students[i])
    else:
        students_1[student].append(cours)
        students_1[student].append(students[i])

print("Ranking:")

for i in students_1:
    print(f"{i}")
    for j in range(0, len(students_1[i]),2):
        print(f"#  {students_1[i][j]} -> {students_1[i][j+1]}")
