def recursive_power(num, power):
    if power == 0:
        return 1
    num *= recursive_power(num, power-1)
    return num

print(recursive_power(2, 10))
print(recursive_power(10, 100))
