def get_magic_triangle(n):
    if n == 2:
        return [[1], [1, 1]]
    triangle = get_magic_triangle(n - 1)
    new_row = []
    for i in range(len(triangle[-1])):
        if i == 0:
            new_row.append(triangle[-1][0])
        else:
            new_row.append(triangle[-1][i - 1] + triangle[-1][i])
    new_row.append(triangle[-1][-1])
    triangle.append(new_row)
    return triangle


print(get_magic_triangle(10))
