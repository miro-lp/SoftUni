n = int(input())
b = input()

counter = 0
for i in bin(n)[2:]:
    if i == b:
        counter += 1

print(counter)