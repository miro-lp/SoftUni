text = input().split(", ")

text = text[::-1]

for index, animal in enumerate(text):
    if index == 0 and animal == "wolf":
        print("Please go away and stop eating my sheep")
    elif index!=0 and animal == "wolf":
        print(f"Oi! Sheep number {index}! You are about to be eaten by a wolf!")
