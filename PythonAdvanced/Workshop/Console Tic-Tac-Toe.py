def setup():
    global player_1,player_2
    player_1_name = input("Player one name: ")
    player_2_name = input("Player two name: ")
    player_1_mark = input(f"{player_1} would you like to play with 'x' or 'o'? ")
    player_2_mark = "o" if player_1 == "x" else "x"
    player_1 = [player_1_name,player_1_mark]
    player_2 = [player_2_name, player_2_mark]
    print("This is the numeration of the board")
    print("| 1 | 2 | 3 |")
    print("| 4 | 5 | 6 |")
    print("| 7 | 8 | 9 |")
    print(f"{player_1_name} starts first!")


player_1 = None
player_2 = None
board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
setup()
current = player_1
other = player_2
loop = True



