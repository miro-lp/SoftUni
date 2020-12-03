version = input().split(".")

num = str(int("".join(version)) + 1)

new_version = [i for i in num]

print(".".join(new_version))
