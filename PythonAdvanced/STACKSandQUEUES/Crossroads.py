from collections import deque

green_l = int(input())
free_w = int(input())

cars = deque()

while True:
    line = input()
    if line == "END":
        break
    cars.append(line)

crossing_cars = deque()
is_crash = False
total_cars_passed = 0
while len(cars) > 0:
    car = cars.popleft()
    if car == "green":
        green_l_now = green_l
        while len(crossing_cars) > 0:
            car_1 = crossing_cars.popleft()
            green_l_now -= len(car_1)
            if green_l_now < 0:
                if green_l_now + free_w < 0:
                    print("A crash happened!")
                    print(f"{car_1} was hit at {car_1[green_l_now + free_w]}.")
                    is_crash = True
                    break
                else:
                    total_cars_passed += 1
                    break
            elif green_l_now == 0:
                total_cars_passed += 1
                break
            else:
                total_cars_passed += 1
    else:
        crossing_cars.append(car)
    if is_crash:
        break
if not is_crash:
    print("Everyone is safe.")
    print(f"{total_cars_passed} total cars passed the crossroads.")
