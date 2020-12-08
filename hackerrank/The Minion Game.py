def minion_game(string):
    vowels = "AEOIU"
    stuart_words = 0
    kevin_words = 0

    for i in range(len(string)):
        if string[i] in vowels:
            kevin_words += (len(string)-i)
        else:
            stuart_words += (len(string)-i)
    if kevin_words > stuart_words:
        print(f"Kevin {kevin_words}")
    elif kevin_words < stuart_words:
        print(f"Stuart {stuart_words}")
    else:
        print("Draw")
    # your code goes here


s = input()
minion_game(s)
