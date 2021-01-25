def numbers_searching(*args):
    miss_num = [i for i in range(min(args), max(args) + 1) if i not in args]
    dupl_nums = set([i for i in args if i in (args[:args.index(i)] + args[args.index(i) + 1:])])
    miss_num.append(sorted(dupl_nums))
    return miss_num


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
