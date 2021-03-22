def minimumBribes(q):
    if len([n for i, n in enumerate(q) if n - (i + 1) > 2]) > 0:
        print("Too chaotic")
        return
    bribes = 0
    in_q = [i for i in range(1, len(q) + 1)]
    i_e =0
    while q != in_q:
        for i, value in enumerate(q[i_e:]):
            if q[i+i_e] != in_q[i+i_e]:
                index = in_q.index(value)
                in_q[index], in_q[index - 1] = in_q[index - 1], in_q[index]
                bribes += 1
                i_e += i

                break

    print(bribes)


t = int(input())

for t_itr in range(t):
    n = int(input())

    q = list(map(int, input().rstrip().split()))

    minimumBribes(q)
