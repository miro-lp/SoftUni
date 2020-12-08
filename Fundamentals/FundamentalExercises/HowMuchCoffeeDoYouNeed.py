counter = 0
is_less_5 = True
while True:
    command = input()
    if command == "END":
        break
    if command == "cat" or command == "dog" or command == "movie" or command == "coding":
        counter += 1
    elif command == "CAT" or command == "DOG" or command == "MOVIE" or command == "CODING":
        counter += 2
    if counter > 5:
        print("You need extra sleep")
        is_less_5 = False
        break
if is_less_5:
    print(counter)
