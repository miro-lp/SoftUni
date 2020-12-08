import math
students = int(input())
lectures = int(input())
bonus = int(input())

max_attendance = 0
for i in range(students):
    attendances = int(input())
    if attendances > max_attendance:
        max_attendance = attendances

if lectures>0:
    total_bonus = max_attendance/lectures*(5+bonus)
    total_bonus = math.ceil(total_bonus)
else:
    total_bonus = 0

print(f"Max Bonus: {total_bonus}.")
print(f"The student has attended {max_attendance} lectures.")