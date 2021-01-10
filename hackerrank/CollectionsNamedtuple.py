from collections import namedtuple

n = int(input())
students = namedtuple('student', input().split())

total = 0
for i in range(n):
    student = students(*input().split())
    total += int(student.MARKS)

print(f'{total / n:.2f}')
