num = int(input())

is_it_prime = True
for i in range(2,num):
    if num%i == 0:
        is_it_prime = False

if is_it_prime:
    print(True)
else:
    print(False)