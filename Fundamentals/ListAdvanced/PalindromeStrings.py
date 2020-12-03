list_of_words = input().split(" ")
searched_palind = input()

palindrome_list = [element for element in list_of_words if element == element[::-1]]

counter = 0
for word in palindrome_list:
    if word == searched_palind:
        counter += 1

print(palindrome_list)
print(f"Found palindrome {counter} times")
