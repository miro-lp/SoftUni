
def diagonalDifference(arr):
    sum_d_l = 0
    sum_d_r = 0
    for i in range(len(arr)):
        sum_d_l +=arr[i][i]
        sum_d_r +=arr[i][len(arr)-1-i]
    return abs(sum_d_l - sum_d_r)



n = int(input().strip())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))


result = diagonalDifference(arr)

print(str(result) + '\n')
