def loading_bar(num):
    counter = 0
    for i in range(0, num, 10):
        counter += 1
    if num < 100:
        print(f"{num}%", end=" ")
        print("[" + "%" * counter + "." * (10 - counter) + "]")
        print("Still loading...")
    else:
        print("100% Complete!")
        print("[%%%%%%%%%%]")


loading_number = int(input())

loading_bar(loading_number)
