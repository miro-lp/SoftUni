# sequence = [i for i in input().split(" ") if i != ""]
# moveis = 0
# is_it_lose = True
# while True:
#     command = input()
#     if command == "end":
#         break
#     indexes = [int(i) for i in command.split() if i != " "]
#     if len(sequence) == 0:
#         print(f"You have won in {moveis} turns!")
#         is_it_lose = False
#         continue
#     else:
#         moveis += 1
#         if indexes[0] < 0 or indexes[0] > len(sequence) - 1 or indexes[1] < 0 or indexes[1] > len(sequence) - 1 or \
#                 indexes[0] == indexes[1]:
#             print("Invalid input! Adding additional elements to the board")
#             add_index = len(sequence) // 2
#             sequence.insert(add_index, ("-" + str(moveis) + "a"))
#             sequence.insert(add_index + 1, ("-" + str(moveis) + "a"))
#         else:
#             if sequence[indexes[0]] == sequence[indexes[1]]:
#                 print(f"Congrats! You have found matching elements - {sequence[indexes[0]]}!")
#                 sequence = [i for i in sequence if i != sequence[indexes[0]] or i != sequence[indexes[1]]]
#             else:
#                 print("Try again!")
#
# if is_it_lose:
#     print("Sorry you lose :(")
#     print(" ".join(sequence))
def play_round(cards, i_1, i_2, moves):
    if i_1==i_2 or i_1 not in range(len(cards)) or i_2 not in range(len(cards)):
        print("Invalid input! Adding additional elements to the board")
        card = f"-{moves}a"
        middle_i = len(cards)//2
        cards.insert(middle_i,card)
        cards.insert(middle_i+1, card)
        return cards
    if cards[i_1]==cards[i_2]:
        element = cards[i_1]
        print(f"Congrats! You have found matching elements - {element}!")
        cards.remove(element)
        cards.remove(element)
        return cards
    print("Try again!")
    return cards


memory_card = input().split()
command = input()

counter = 0

while command != "end":
    i_1, i_2 = [int(i) for i in command.split()]
    counter += 1
    memory_card = play_round(memory_card, i_1, i_2, counter)
    if len(memory_card) == 0:
        print(f"You have won in {counter} turns!")
        exit(0)
    command = input()

print("Sorry you lose :(")
print(" ".join(memory_card))
