def aVeryBigSum(ar):
    return sum(ar)

ar_count = int(input())

ar = list(map(int, input().rstrip().split()))

result = aVeryBigSum(ar)
print(str(result) + '\n')


