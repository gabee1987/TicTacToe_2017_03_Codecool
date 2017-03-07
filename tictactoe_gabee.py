# import main modules
import time
import os
import random

#Define the board items as a list
board=['-' for x in range(9)]

#Print the header of the Game
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


    Welcome to the greatest intellectual challenge of all time: Tic-Tac-Toe.           
    You will make your move by entering a number, 0 - 8. The number
    will correspond to the board position as illustrated:

                                         0 | 1 | 2
                                        -----------
                                         3 | 4 | 5
                                        -----------
                                         6 | 7 | 8                                                                              
    
    Prepare yourself! The ultimate battle is about to begin.
    """
    print(header)

print_header()

#Print the board
def print_board(board):
    print(' ',board[0],'|',board[1],'|',board[2])
    print(" ---+---+---")
    print(' ',board[3],'|',board[4],'|',board[5])
    print(" ---+---+---")
    print(' ',board[6],'|',board[7],'|',board[8])
print_board(board)

#Check winner rules
def check_win(X):
    if (board[0] == X and board[1] == X and board[2] == X) or \
        (board[3] == X and board[4] == X and board[5] == X) or \
        (board[6] == X and board[7] == X and board[8] == X) or \
        (board[0] == X and board[3] == X and board[6] == X) or \
        (board[1] == X and board[4] == X and board[7] == X) or \
        (board[2] == X and board[5] == X and board[8] == X) or \
        (board[0] == X and board[4] == X and board[8] == X) or \
        (board[2] == X and board[4] == X and board[6] == X):
        return True
    else:
        False

def check_win(O):
    if (board[0] == O and board[1] == O and board[2] == O) or \
        (board[3] == O and board[4] == O and board[5] == O) or \
        (board[6] == O and board[7] == O and board[8] == O) or \
        (board[0] == O and board[3] == O and board[6] == O) or \
        (board[1] == O and board[4] == O and board[7] == O) or \
        (board[2] == O and board[5] == O and board[8] == O) or \
        (board[0] == O and board[4] == O and board[8] == O) or \
        (board[2] == O and board[4] == O and board[6] == O):
        return True
    else:
        False

#Clear screen and print the board
#while True:
    #os.system('clear')
    #print_board()


#Define the player X moves
def player1_move():
    player1_move = int(input("Please take your move, select an empty space for X"))
    print_board(board)

    #Check the move is available or not
    if board[player1_move] == "-":
        board[player1_move] = "X"
    else:
        print("Sorry, that space is already taken")
        time.sleep(2)
    os.system('clear')
    print_board(board)

    #Check for X win
    if check_win('X') == True:
        os.system('clear')
        print_board(board)
        print("Congratulations! Player X won!")
    else:
        player2_move()

    
    #Define the player O moves
def player2_move():
    player2_move = int(input("Please take your move, select an empty space for O"))
    print_board(board)

    #Check the move is available or not
    if board[player2_move] == "-":
        board[player2_move] = "O"
    else:
        print("sorry, that space is already taken")
        time.sleep(2)
    os.system('clear')
    print_board(board)

    #Check for O win
    if check_win('O') == True:
        os.system('clear')
        print_board(board)
        print("Congratulations! Player O won!")
    else:
        player1_move()

player1_move()
player2_move()

#else:
    #print ("GAME OVER")


