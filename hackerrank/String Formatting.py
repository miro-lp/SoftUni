def print_formatted(number):
    for i in range(1, number + 1):
        print(
            str(i).rjust(len(bin(number)[1:]))
            + str(oct(i))[2:].rjust(len(bin(number)[1:]))
            + str(hex(i))[2:].upper().rjust(len(bin(number)[1:]))
            + str(bin(i))[2:].rjust(len(bin(number)[1:]))
        )

n = int(input())
print_formatted(n)
