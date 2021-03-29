price = int(input())

# count_coins_10 = 0
# for i in range(len(str(price)) - 1, -1, -1):
#     count_coins_10 += price // 10 ** i
#     price -= price // 10 ** i*10**i

count_coins_25 = 0
for i in range(len(str(price)) - 1, -1, -1):
    divider_10 = 10 ** i
    divider_25 = 25 * 100 ** i

    count_coins_25 += price // divider_25
    price -= price // divider_25 * divider_25

    count_coins_25 += price // 10 ** i
    price -= price // 10 ** i * 10 ** i

print(count_coins_25)
