n, m = input().split()
arr = input().split()
arr_like = set(input().split())
arr_dislike = set(input().split())


print(([(i in arr_like)-(i in arr_dislike)for i in arr]))

