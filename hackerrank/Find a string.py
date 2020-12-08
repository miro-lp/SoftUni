def count_substring(string, sub_string):
    counter = 0
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i + len(sub_string)] == sub_string:
            counter += 1
    return counter


string = input().strip()
sub_string = input().strip()

count = count_substring(string, sub_string)
print(count)
