key = int(input())
num = int(input())

message = [input() for i in range(num)]

real_message = [chr(ord(i) + key) for i in message]

print("".join(real_message))
