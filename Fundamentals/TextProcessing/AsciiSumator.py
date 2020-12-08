start = input()
finish = input()
text = input()

sum = 0

for i in text:
    if ord(start)<ord(i)<ord(finish):
        sum+=ord(i)

print(sum)