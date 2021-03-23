def read_next(*args):
    for text in args:
        for i in text:
            yield str(i)

for item in read_next('string', (2,), {'d': 1, 'i': 2, 'c': 3, 't': 4}):
    print(item, end='')
