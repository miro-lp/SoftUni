def candies(n, arr):
    s = [0] * n
    c = [0] * n
    for i in range(len(arr)):
        if i == 0 or s[i - 1] == 1:
            s[i] = get_num_descending(arr, i)
        else:
            s[i] = s[i - 1] - 1
        c[i] = s[i] if arr[i] <= arr[i - 1] else max(s[i], c[i - 1] + 1)
    return sum(c)


def get_num_descending(arr, i):
    '''
    Returns the length of decreasing sequence, starting at position i.
    '''
    ret = 1
    while i + 1 < len(arr):
        if arr[i] > arr[i + 1]:
            ret += 1
            i += 1
        else:
            return ret
    return ret


n = int(input())

arr = []

for _ in range(n):
    arr_item = int(input())
    arr.append(arr_item)

result = candies(n, arr)

print(result)
