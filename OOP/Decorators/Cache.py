from functools import wraps


def cache(func):
    func.log = {}

    @wraps(func)
    def wrapper(n):
        if n not in func.log:
            func.log[n] = func(n)
        return func.log[n]

    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(3)
print(fibonacci.log)
fibonacci(8)
print(fibonacci.log)
