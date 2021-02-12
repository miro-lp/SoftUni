from collections import deque

males = list(map(int, input().split()))
females = (map(int, input().split()))

males = [i for i in males if i >0]
females = deque([i for i in females if i >0])
matches = 0
while len(females) > 0 and len(males) > 0:
    f = females[0]
    while len(males) > 0 and males[-1] <= 0:
        males.pop()
    if f > 0 and f % 25 != 0:
        if len(males) > 0 and males[-1] % 25 == 0 and males[-1] >= 25:
            males.pop()
            if len(males) > 0:
                males.pop()
        if len(males) > 0 and males[-1] == f:
            matches += 1
            males.pop()
            females.popleft()
        elif len(males) > 0:
            males[-1] -= 2
            females.popleft()
    elif f % 25 == 0 and f != 0:
        females.popleft()
        if len(females) > 0:
            females.popleft()
    else:
        while len(females) > 0 and females[0] <= 0:
            females.pop()


print(f"Matches: {matches}")
if len(males) == 0:
    print("Males left: none")
else:
    print(f"Males left: {', '.join(map(str, males[::-1]))}")
if len(females) == 0:
    print("Females left: none")
else:
    print(f"Females left: {', '.join(map(str, females))}")
