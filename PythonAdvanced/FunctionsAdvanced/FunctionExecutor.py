def func_executor (*args):
    res = []
    for i in args:
        tuples = i[1]
        res.append(i[0](*tuples))
    return res

