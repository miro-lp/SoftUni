def nearest_point(x_1, y_1, x_2, y_2):
    hypo_1 = x_1 ** 2 + y_1 ** 2
    hypo_2 = x_2 ** 2 + y_2 ** 2
    if hypo_1 <= hypo_2:
        print("(" + str(int(x_1)) + ", " + str(int(y_1)) + ")")
    else:
        print("(" + str(int(x_2)) + ", " + str(int(y_2)) + ")")


x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())

nearest_point(x_1, y_1, x_2, y_2)
