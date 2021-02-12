prthns = input()
is_balanced = True
openings = []

mirror = {"{": "}", "[": "]", "(": ")"}

for p in prthns:
    if p in "{[(":
        openings.append(p)
    else:
        if len(openings)==0:
            is_balanced = False
            break
        current = openings.pop()
        if not p == mirror[current]:
            is_balanced = False
            break
if is_balanced and len(openings)==0:
    print("YES")
else:
    print("NO")

