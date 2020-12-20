text = input()

count_ocurr = {}

for c in text:
    if c not in count_ocurr:
        count_ocurr[c] = 0
    count_ocurr[c] += 1

count_ocurr = dict(sorted(count_ocurr.items(), key= lambda x: x[0]))

for key in count_ocurr:
    print(f"{key}: {count_ocurr[key]} time/s")
