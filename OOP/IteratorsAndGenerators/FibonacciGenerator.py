def fibonacci():
    n = 0
    m = 1
    while True:
        yield n
        k = n
        n = m
        m += k


generator = fibonacci()
for i in range(10):
    print(next(generator))
