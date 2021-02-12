from math import ceil


def setup():
    global player_1, player_2
    player_1_name = input("Player one name: ")
    player_2_name = input("Player two name: ")
    player_1_mark = input(f"{player_1} would you like to play with 'x' or 'o'? ")
    player_2_mark = "o" if player_1_mark == "x" else "x"
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
    first_row = all([x == current[1] for x in board[0]])
    second_row = all([x == current[1] for x in board[1]])
    third_row = all([x == current[1] for x in board[2]])
    first_column = all([x == current[1] for x in [board[0][0], board[1][0], board[2][0]]])
    second_column = all([x == current[1] for x in [board[0][1], board[1][1], board[2][1]]])
    third_column = all([x == current[1] for x in [board[0][2], board[1][2], board[2][2]]])
    first_diagonal = all([x == current[1] for x in [board[0][0], board[1][1], board[2][2]]])
    secod_diagonal = all([x == current[1] for x in [board[0][2], board[1][1], board[2][0]]])
    if any([first_row, second_row, third_row, first_column, second_column, third_column, first_diagonal,
            secod_diagonal]):
        print(f"{current[0]} won!")
        loop = False


def play(current_local, board):
    global current, other
    choice = int(input(f"{current_local[0]} choose a free position [1:9]: "))
    if choice not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        print("Invalid! Try again")
        current, other = other, current
    else:
        row = ceil(choice / 3) - 1
        col = choice % 3 - 1
        if board[row][col] == " ":
            board[row][col] = current_local[1]
            draw_board(board)
            check_if_win(current_local, board)
        else:
            print("Invalid! Try again")
            current, other = other, current


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
