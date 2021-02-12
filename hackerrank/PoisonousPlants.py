def poisonousPlants(p):
    new_p = []
    counter = 0
    len_p = len(p)
    is_dead = True
    while is_dead:
        if len(p)>0:
            f = p.pop()
            if len(p)>0:
                if f > p[-1]:
                    continue
            new_p.insert(0,f)
        else:
            p = new_p
            if len(p)==len_p:
                is_dead = False
            else:
                counter += 1
                new_p=[]
                len_p = len(p)
    return counter


n = int(input())

p = list(map(int, input().rstrip().split()))

print(poisonousPlants(p))
