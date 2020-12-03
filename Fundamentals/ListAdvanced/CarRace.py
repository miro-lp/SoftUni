def sum_of_times(time_list):
    n = len(time_list) // 2
    total_time = 0
    for i in range(n):
        if time_list[i] != 0:
            total_time += time_list[i]
        else:
            total_time *= 0.8
    return total_time


time_list = list(map(int, input().split(" ")))

time_left = sum_of_times(time_list)
time_right = sum_of_times(time_list[::-1])

if time_right > time_left:
    print(f"The winner is left with total time: {time_left:.1f}")
else:
    print(f"The winner is right with total time: {time_right:.1f}")
