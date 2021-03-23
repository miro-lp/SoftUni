def get_primes(nums):
    return (i for i in nums if len([k for k in range(2, i) if i % k == 0]) == 0 and i > 1)


print(list(get_primes([103, 105, 2, 4, 3, 5, 6, 9, 23, 1, 0, 53, 97, 101])))
