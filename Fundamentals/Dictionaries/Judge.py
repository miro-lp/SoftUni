contests = {}
students = {}

while True:
    data = input()
    if data == "no more time":
        break
    name, course, points = data.split(" -> ")
    if course not in contests:
        contests[course] = {name: int(points)}
    else:
        if name not in contests[course]:
            contests[course][name] = int(points)
        elif contests[course][name] < int(points):
            contests[course][name] = int(points)

for i in contests:
    for j in contests[i].keys():
        if j not in students:
            students[j] = []
        students[j].append(contests[i][j])
for k in contests:
    contests[k] = dict(sorted(contests[k].items(), key= lambda x: (-x[1], x[0])))

students = dict(sorted(students.items(), key= lambda y: (-sum(y[1]), y[0])))
for i in contests:
    print(f"{i}: {len((contests[i]))} participants")
    count = 0
    for j in contests[i].keys():
        count += 1
        print(f"{count}. {j} <::> {contests[i][j]}")
print("Individual standings:")
stud_count = 0
for k in students:
    stud_count += 1
    print(f"{stud_count}. {k} -> {sum(students[k])}")
