from collections import deque

prnths = deque(input())

index = 0

for _ in range(len(prnths) // 2):
    if ord(prnths[index]) == ord(prnths[1 + index]) - 2 or prnths[index] == "(" and prnths[
        1 + index] == ")":
        prnths.popleft()
        prnths.popleft()
    elif ord(prnths[index]) == ord(prnths[len(prnths) - 1 - index]) - 2 or prnths[index] == "(" and \
            prnths[len(prnths) - 1 - index] == ")":
        prnths.popleft()
        prnths.pop()

if len(prnths) == 0:
    print("YES")
else:
    print("NO")
