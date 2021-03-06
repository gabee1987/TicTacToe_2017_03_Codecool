# Import main modules
import time
import os
import random
import sys

# Define the board items as a list
board = [0] + ['-' for x in range(9)]
score_x = 0
score_o = 0
score_c = 0
score_tie = 0


def print_score():
    if select == 'p':
        print('Score: \nPlayer X:', score_x, '| Player O:', score_o, '| Tie:', score_tie, '\n')
    elif select == 'c' or 'hc':
        print('Score: \nPlayer:', score_x, '| Computer:', score_c, '| Tie:', score_tie, '\n')


# Print the board
def print_board(board):
    print_score()
    print(' ', board[7], '|', board[8], '|', board[9])
    print(" ---+---+---")
    print(' ', board[4], '|', board[5], '|', board[6])
    print(" ---+---+---")
    print(' ', board[1], '|', board[2], '|', board[3], '\n')


# Define the player X moves
def player_x_move():
    error = 1
    while error == 1:
        try:
            player_x_move = int(input("Please take your move, select an empty space for X : "))
            if player_x_move == board[0]:
                print("\nSorry, that\'s not a valid move. Try again! ")
                time.sleep(1)
                error = 1
            elif board[player_x_move] == "-":        # Check the move is available or not
                board[player_x_move] = "X"
                error = 0
            else:
                print("\nSorry, that\'s not a valid move. Try again! ")
                time.sleep(1)
                error = 1
        except ValueError:                          # Ask for take a move again if the input is not a number
            print("\nSorry, that\'s not a valid move. Try again! ")
            time.sleep(1)
        except IndexError:
            print("\nSorry, that\'s not a valid move. Try again! ")
            time.sleep(1)
        os.system('clear')
        print_board(board)


# Define the player O moves
def player_o_move():
    error = 1
    while error == 1:
        try:
            player_o_move = int(input("Please take your move, select an empty space for O : "))
            if player_o_move == board[0]:
                print("\nSorry, that\'s not a valid move. Try again! ")
                time.sleep(1)
                player_o_move()
                error = 1
            elif board[player_o_move] == "-":    # Check the move is available or not
                board[player_o_move] = "O"
                error = 0
            else:
                print("\nSorry, that\'s not a valid move. Try again! ")
                time.sleep(1)
                error = 1
        except ValueError:                      # Ask for take a move again if the input is not a number
            print("\nThat's not a number. Try again")
            time.sleep(1)
        except IndexError:
            print("\nSorry, that\'s not a valid move. Try again! ")
            time.sleep(1)
        os.system('clear')
        print_board(board)


def computer():
    move = 0
    for x in range(0, 4):
        dots = " Thinking" + "." * x
        print (dots, end="\r")
        time.sleep(0.1)
    time.sleep(0.1)
    while move == 0: 
        f = random.randint(1, 9)
        if board[f] == '-':
            board[f] = 'O'
            move = 1
        os.system('clear')
        print_board(board)


def hc_computer():
    for x in range(0, 4):
        dots = " Thinking" + "." * x
        print (dots, end="\r")
        time.sleep(0.5)
    time.sleep(0.1)
    if board[5] == '-':
        board[5] = 'O'
        os.system('clear')
        print_board(board)
        return
    # Do I win this turn?
    r = boardwincheck_o(7, 8, 9)
    if r is not None:
        if board[r] == '-':
            board[r] = 'O'
            os.system('clear')
            print_board(board)
            return
    r = boardwincheck_o(4, 5, 6)
    if r is not None:
        if board[r] == '-':
            board[r] = 'O'
            os.system('clear')
            print_board(board)
            return
    r = boardwincheck_o(1, 2, 3)
    if r is not None:
        if board[r] == '-':
            board[r] = 'O'
            os.system('clear')
            print_board(board)
            return
    r = boardwincheck_o(7, 4, 1)
    if r is not None:
        if board[r] == '-':
            board[r] = 'O'
            os.system('clear')
            print_board(board)
            return
    r = boardwincheck_o(8, 5, 2)
    if r is not None:
        if board[r] == '-':
            board[r] = 'O'
            os.system('clear')
            print_board(board)
            return
    r = boardwincheck_o(9, 6, 3)
    if r is not None:
        if board[r] == '-':
            board[r] = 'O'
            os.system('clear')
            print_board(board)
            return
    r = boardwincheck_o(7, 5, 3)
    if r is not None:
        if board[r] == '-':
            board[r] = 'O'
            os.system('clear')
            print_board(board)
            return
    r = boardwincheck_o(9, 5, 1)
    if r is not None:
        if board[r] == '-':
            board[r] = 'O'
            os.system('clear')
            print_board(board)
            return
    # Does player win next turn?
    r = boardwincheck_x(7, 8, 9)
    if r is not None:
        if board[r] == '-':
            board[r] = 'O'
            os.system('clear')
            print_board(board)
            return
    r = boardwincheck_x(4, 5, 6)
    if r is not None:
        if board[r] == '-':
            board[r] = 'O'
            os.system('clear')
            print_board(board)
            return
    r = boardwincheck_x(1, 2, 3)
    if r is not None:
        if board[r] == '-':
            board[r] = 'O'
            os.system('clear')
            print_board(board)
            return
    r = boardwincheck_x(7, 4, 1)
    if r is not None:
        if board[r] == '-':
            board[r] = 'O'
            os.system('clear')
            print_board(board)
            return
    r = boardwincheck_x(8, 5, 2)
    if r is not None:
        if board[r] == '-':
            board[r] = 'O'
            os.system('clear')
            print_board(board)
            return
    r = boardwincheck_x(9, 6, 3)
    if r is not None:
        if board[r] == '-':
            board[r] = 'O'
            os.system('clear')
            print_board(board)
            return
    r = boardwincheck_x(7, 5, 3)
    if r is not None:
        if board[r] == '-':
            board[r] = 'O'
            os.system('clear')
            print_board(board)
            return
    r = boardwincheck_x(9, 5, 1)
    if r is not None:
        if board[r] == '-':
            board[r] = 'O'
            os.system('clear')
            print_board(board)
            return
    # Is 1 3 7 9 free?
    for _ in range(5):
        corners = [1, 3, 7, 9]
        s = random.choice(corners)
        if board[s] == '-':
            board[s] = 'O'
            os.system('clear')
            print_board(board)
            return
    # Is 2 4 6 8 free?
    for _ in range(5):
        notcorners = [2, 4, 6, 8]
        s = random.choice(notcorners)
        if board[s] == '-':
            board[s] = 'O'
            os.system('clear')
            print_board(board)
            return


def boardwincheck_o(f, g, j):
    if board[f] == board[g] == 'O':
        return j
    if board[f] == board[j] == 'O':
        return g
    if board[g] == board[j] == 'O':
        return f


def boardwincheck_x(f, g, j):
    if board[f] == board[g] == 'X':
        return j
    if board[f] == board[j] == 'X':
        return g
    if board[g] == board[j] == 'X':
        return f


def pvp_or_pvc_or_pvhc():
    error = 0
    while error == 0:
        if select == 'p':
            error = 1
            pvp()
        elif select == 'c':
            error = 1
            pvc()
        elif select == 'hc':
            error = 1
            pvhc()
        else:
            error = 0


# Randomly select which player starts
def player_select(rp):
    rp = random.randint(0, 1)
    if rp == 0:
        print('Player X will start the game')
    else:
        print('Player O will start the game')
    return rp


# Check winner
def check_win(X):
    if (board[7] == X and board[8] == X and board[9] == X) or \
        (board[4] == X and board[5] == X and board[6] == X) or \
        (board[1] == X and board[2] == X and board[3] == X) or \
        (board[7] == X and board[4] == X and board[1] == X) or \
        (board[8] == X and board[5] == X and board[2] == X) or \
        (board[9] == X and board[6] == X and board[3] == X) or \
        (board[7] == X and board[5] == X and board[3] == X) or \
       (board[9] == X and board[5] == X and board[1] == X):
        return True
    else:
        False


# Ask the player for a new game
def endofgame():
    newgame = input("Do you want to play again? Y or N? : ")
    if newgame == "Y" or newgame == "y":
            for i in range(len(board)):
                board[i] = '-'
            os.system('clear')
            print_board(board)
            for x in range(0, 4):
                dots = " Random selecting player" + "." * x
                print (dots, end="\r")
                time.sleep(0.2)
            pvp_or_pvc_or_pvhc()
    elif newgame == "N" or newgame == "n":
            print("What\'s wrong? CHICKEN??")
            time.sleep(2)
            quit()
    else:
        endofgame()


# Print the header of the Game
def print_header():
    header = """
                88888888888 8888888 .d8888b. 88888888888     d8888  .d8888b. 88888888888 .d88888b.  8888888888
                    888       888  d88P  Y88b    888        d88888 d88P  Y88b    888    d88P" "Y88b 888
                    888       888  888    888    888       d88P888 888    888    888    888     888 888
                    888       888  888           888      d88P 888 888           888    888     888 8888888
                    888       888  888           888     d88P  888 888           888    888     888 888
                    888       888  888    888    888    d88P   888 888    888    888    888     888 888
                    888       888  Y88b  d88P    888   d8888888888 Y88b  d88P    888    Y88b. .d88P 888
                    888     8888888 "Y8888P"     888  d88P     888  "Y8888P"     888     "Y88888P"  8888888888
                                                        +-++-+ +-++-++-++-++-++-++-++-++-++-+ +-+ +-++-++-++-++-+
                                                        |b||y| |s||i||x||p||i||s||t||o||l||s| |&| |G||a||b||e||e|
                                                        +-++-+ +-++-++-++-++-++-++-++-++-++-+ +-+ +-++-++-++-++-+
                            Welcome to the greatest intellectual challenge of all time: Tic-Tac-Toe.
                            You will make your move by entering a number on the numpad, 1 - 9. The number
                            will correspond to the board position as illustrated:
                                                     7 | 8 | 9
                                                    ---+---+---
                                                     4 | 5 | 6
                                                    ---+---+---
                                                     1 | 2 | 3
                            Prepare yourself! The ultimate battle is about to begin.

                            To play against friend, write: p
                            To play against easy computer, write: c
                            To play against hard computer, write: hc
    """
    print(header)


def pvp():
    os.system('clear')
    print_board(board)
    rp = random.randint(0, 1)                # Select which player starts
    if rp == 0:
        print('Player X will start the game')
    else:
        print('Player O will start the game')
    turn = 0
    while turn < 9:
        if rp == 0:
            rp += 1
            player_x_move()
            turn += 1
            if check_win('X') is True:      # Check for X win
                os.system('clear')
                print_board(board)
                print("Congratulations! Player X won!")
                global score_x
                score_x += 1
                endofgame()
        else:
            rp -= 1
            player_o_move()
            turn += 1
            if check_win('O') is True:      # Check for O win
                os.system('clear')
                print_board(board)
                print("Congratulations! Player O won!")
                global score_o
                score_o += 1
                endofgame()
    else:
        print("The game is a TIE.")
        global score_tie
        score_tie += 1
        endofgame()


def pvc():
    os.system('clear')
    print_board(board)
    rp = random.randint(0, 1)                # Select which player starts
    if rp == 0:
        print('You will start the game')
    else:
        print('Computer will start the game')
    turn = 0
    while turn < 9:
        if rp == 0:
            rp += 1
            player_x_move()
            turn += 1
            if check_win('X') is True:      # Check for X win
                os.system('clear')
                print_board(board)
                print("Congratulations! Player X won!")
                global score_x
                score_x += 1
                endofgame()
        else:
            rp -= 1
            computer()
            turn += 1
            if check_win('O') is True:      # Check for O win
                os.system('clear')
                print_board(board)
                print("Sorry dude, the computer won.")
                global score_c
                score_c += 1
                endofgame()
    else:
        print("The game is a TIE.")
        global score_tie
        score_tie += 1
        endofgame()


def pvhc():
    os.system('clear')
    print_board(board)
    rp = random.randint(0, 1)                # Select which player starts
    if rp == 0:
        print('You will start the game')
    else:
        print('Computer will start the game')
    global turn
    turn = 0
    while turn < 9:
        if rp == 0:
            rp += 1
            player_x_move()
            turn += 1
            if check_win('X') is True:      # Check for X win
                os.system('clear')
                print_board(board)
                print("Congratulations! Player X won!")
                global score_x
                score_x += 1
                endofgame()
        else:
            rp -= 1
            hc_computer()
            turn += 1
            if check_win('O') is True:      # Check for O win
                os.system('clear')
                print_board(board)
                print("Sorry dude, the computer won.")
                global score_c
                score_c += 1
                endofgame()
    else:
        print("The game is a TIE.")
        global score_tie
        score_tie += 1
        endofgame()


def main():
    global select
    select = input('Please select game mode:')
    pvp_or_pvc_or_pvhc()


print_header()
main()