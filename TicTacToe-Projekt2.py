
# """
# projekt_2.py: druhý projekt do Engeto Online Python Akademie
# author: Tomas Kupka 
# email: tomaskupka93@gmail.com
# discord: Tomas.K
# """


field = [' ' for b in range(9)]

game_go = True
winner = None
current_player = "X"


def play_game():
    # display initial board
    display_board()

    while game_go:
        global current_player

        print(spacer)

        move = input(f"Player {current_player} | Please enter your move, choose number "
                     f"(1-9): ")
        try:
            move_n = int(move)
            if (move_n >= 1) and (move_n <= 9):
                position = int(move_n) - 1
                if space_free(position):
                    field[position] = current_player
                    display_board()
                else:
                    print("The field is taken! Try it again!")
                    continue
            else:
                print('Please number between 1 - 9')
                continue
        except :
            print("is not number, try it again! ")
            continue

        check_win()
        check_tie()

        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

    if (winner == "X") or (winner == "O"):
        print(f" Player {winner} congratulation WON!")
    else:
        print("All fields are filled, GAME OVER. It's a DRAW!")


def display_board():
    print("+---+---+---+")
    print(f"| {field[0]} | {field[1]} | {field[2]} |")
    print("+---+---+---+")
    print(f"| {field[3]} | {field[4]} | {field[5]} |")
    print("+---+---+---+")
    print(f"| {field[6]} | {field[7]} | {field[8]} |")
    print("+---+---+---+")


def check_win():
    global winner

    win_row = check_rows()
    win_column = check_columns()
    win_dig = check_diagonals()
    if win_row:
        winner = win_row
    elif win_column:
        winner = win_column
    elif win_dig:
        winner = win_dig
    else:
        winner = None


def check_rows():

    global game_go

    row_1 = field[0] == field[1] == field[2] != " "
    row_2 = field[3] == field[4] == field[5] != " "
    row_3 = field[6] == field[7] == field[8] != " "
    if row_1 or row_2 or row_3:
        game_go = False
    if row_1:
        return field[0]
    elif row_2:
        return field[3]
    elif row_3:
        return field[6]
    else:
        return None


def check_columns():

    global game_go

    column_1 = field[0] == field[3] == field[6] != " "
    column_2 = field[1] == field[4] == field[7] != " "
    column_3 = field[2] == field[5] == field[8] != " " 
    if column_1 or column_2 or column_3:
        game_go = False
    if column_1:
        return field[0]
    elif column_2:
        return field[1]
    elif column_3:
        return field[2]
    else:
        return None


def check_diagonals():

    global game_go

    diagonal_1 = field[0] == field[4] == field[8] != " "
    diagonal_2 = field[6] == field[4] == field[2] != " "
    if diagonal_1 or diagonal_2:
        game_go = False
    if diagonal_1:
        return field[0]
    elif diagonal_2:
        return field[2]
    else:
        return None


def check_tie():
    global game_go
    if " " not in field:
        game_go = False
        return True
    else:
        return False


def space_free(position):
    return field[position] == ' '


spacer = "°" * 50
print(spacer, "   Welcome in the game Tic Tac Toe", spacer, sep="\n")
print("     The rules of the game ")
print(spacer)
print('''Two players placing alternately on the play field their symbols X/O.
The winner is the one who occupy 3 same symbols  adjoining fields. 
in a row, in the colum or diagonaly.
You can place the symbols by pressing any number in to empty field from 1-9.
Press any key to start the game, good luck. ''')
print(spacer)
print("{0:^50}".format("Let's start the game"))
print('-' * 50)

play_game()