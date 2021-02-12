jobs = list(map(int, input().split(", ")))
index = int(input())

sorted_jobs = sorted(jobs)

cycles = 0
for i in sorted_jobs:
    ind = jobs.index(i)
    if ind == index:
        cycles += i
        break
    cycles += i
    jobs[ind] = "*"

print(cycles)
