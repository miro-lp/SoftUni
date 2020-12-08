n = int(input())
snowball_value = 0
snowball_value_max = 0
snowball_snow_last = 0
snowball_time_last = 0
snowball_quality_last = 0
for i in range(n):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = int((snowball_snow / snowball_time) ** snowball_quality)
    if snowball_value > snowball_value_max:
        snowball_value_max = snowball_value
        snowball_snow_last = snowball_snow
        snowball_time_last = snowball_time
        snowball_quality_last = snowball_quality

# {snowballSnow} : {snowballTime} = {snowballValue} ({snowballQuality})
print(f"{snowball_snow_last} : {snowball_time_last} = {snowball_value_max} ({snowball_quality_last})")
