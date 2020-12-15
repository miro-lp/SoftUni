from collections import deque

n = int(input())
petrol_pumps_first = deque()

for i in range(n):
    line = [int(i) for i in input().split()]
    ratio_fuel_km = line[0] - line[1]
    petrol_pumps_first.append(ratio_fuel_km)

for i in range(n):
    start_index = 0
    start_fuel = 0
    if petrol_pumps_first[i] > 0:
        start_index = i
        petrol_pumps = deque([i for i in petrol_pumps_first])
        petrol_pumps.rotate((-i))
        while len(petrol_pumps) > 0:
            start_fuel += petrol_pumps.popleft()
            if start_fuel < 0:
                break
        if start_fuel >= 0:
            print(start_index)
            break
