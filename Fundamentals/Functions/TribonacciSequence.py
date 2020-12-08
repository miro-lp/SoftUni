def tribonacci_sequence(num):
    trib_list = [1, 1, 2]
    if num >= 3:
        for i in range(3, num):
            next_num = trib_list[i - 1] + trib_list[i - 2] + trib_list[i - 3]
            trib_list.append(next_num)
    elif num == 2:
        trib_list = [1, 1]
    else:
        trib_list = [1]
    trib_list = [str(i) for i in trib_list]
    return " ".join(trib_list)


n = int(input())

print(tribonacci_sequence(n))
