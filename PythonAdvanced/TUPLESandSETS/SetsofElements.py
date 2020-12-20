n, m = map(int, input().split())

set_n = set([input() for _ in range(n)])
set_m = set([input() for _ in range(m)])

print("\n".join(set_n & set_m))
