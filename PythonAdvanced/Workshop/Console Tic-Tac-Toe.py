from math import ceil


def setup():
    global player_1, player_2
    player_1_name = input("Player one name: ")
    player_2_name = input("Player two name: ")
    player_1_mark = input(f"{player_1} would you like to play with 'x' or 'o'? ")
    player_2_mark = "o" if player_1 == "x" else "x"
    player_1 = [player_1_name, player_1_mark]
    player_2 = [player_2_name, player_2_mark]
    print("This is the numeration of the board")
    print("| 1 | 2 | 3 |")
    print("| 4 | 5 | 6 |")
    print("| 7 | 8 | 9 |")
    print(f"{player_1_name} starts first!")


def draw_board(board):
    for row in board:
        print("| ", end="")
        print(" | ".join([str(i) for i in row]), end="")
        print(" |")


def check_if_win(current, board):
    global loop
    all()
    pass


def play(current, board):
    choice = int(input(f"{current[0]} choose a free position [1:9]: "))
    row = ceil(choice / 3) - 1
    col = choice % 3 - 1
    board[row][col] = current[1]
    draw_board(board)
    check_if_win(current, board)


player_1 = None
player_2 = None
board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
setup()
current = player_1
other = player_2
loop = True

while loop:
    play(current, board)
    current, other = other, current
