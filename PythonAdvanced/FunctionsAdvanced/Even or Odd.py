def even_odd(*args):
    if args[-1] == "odd":
        args = list(filter(lambda x: x % 2 == 1, map(int, args[:-1])))
    else:
        args = list(filter(lambda x: x % 2 == 0, map(int, args[:-1])))
    return args
