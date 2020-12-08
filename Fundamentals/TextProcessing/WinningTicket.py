tickets = input().split(', ')
valid = '@#$^'


def max_repeating(string, symbol):
    if symbol not in string:
        return 0

    max_count = 0
    curr_count = 0

    for i in range(len(string)):
        if string[i] == symbol:
            curr_count += 1
        else:
            if max_count < curr_count:
                max_count = curr_count
            curr_count = 0

    return max(max_count, curr_count)


for t in tickets:
    t = t.strip()
    if len(t) != 20:
        print(f'invalid ticket')
        continue

    match = False
    Jack = False

    middle = len(t) // 2
    first = t[:middle]
    second = t[middle:]

    for v in valid:
        if t.count(v) == 20:
            Jack = True
            print(f'ticket "{t}" - {10}{v} Jackpot!')
            break

        f = max_repeating(first, v)
        s = max_repeating(second, v)

        if 6 <= f <= 10 and 6 <= s <= 10:
            match = True
            print(f'ticket "{t}" - {min(f, s)}{v}')
            break

    if not match and not Jack:
        print(f'ticket "{t}" - no match')
