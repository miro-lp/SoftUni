from collections import deque


def time_print(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%02d:%02d:%02d" % (hour, minutes, seconds)


robots = [i.split("-") for i in input().split(";")]
start_time = [int(i) for i in input().split(":")]
start_time_sec = start_time[0] * 3600 + start_time[1] * 60 + start_time[2]

products = deque()

while True:
    line = input()
    if line == "End":
        break
    products.append(line)

counter = len(products)

time_robots = {}
for i in range(1, len(robots) + 1):
    time_robots[robots[i - 1][0]] = []
    if int(robots[i - 1][1]) >0:
        for j in range(0, counter * int(robots[i - 1][1]), int(robots[i - 1][1])):
            time_robots[robots[i - 1][0]].append(start_time_sec + i + j)
    else:
        for j in range(counter):
            time_robots[robots[i - 1][0]].append(start_time_sec+i+j)

time = start_time_sec
while len(products) > 0:
    time += 1
    for key in time_robots:
        if time in time_robots[key]:
            print(f"{key} - {products.popleft()} [{time_print(time)}]")
            products.rotate(1)
            break
    products.rotate(-1)

