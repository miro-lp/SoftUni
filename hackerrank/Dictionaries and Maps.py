n = int(input())
phone_book = {}
for i in range(n):
    name, number = input().split()
    phone_book[name] = number


while True:
    line = input()
    if len(line)==0:
        break
    if line not in phone_book:
        print("Not found")
    else:
        print(f"{line}={phone_book[line]}")
