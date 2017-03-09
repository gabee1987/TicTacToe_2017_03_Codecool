#Import main modules
import time
import os
import random

#Define the board items as a list
board=[None] + ['-' for x in range(9)]


#Print the board
def print_board(board):
    print(' ',board[7],'|',board[8],'|',board[9])
    print(" ---+---+---")
    print(' ',board[4],'|',board[5],'|',board[6])
    print(" ---+---+---")
    print(' ',board[1],'|',board[2],'|',board[3])


#Define the player X moves
def player1_move():
    error = 1
    while error == 1:
        try:
            player1_move = int(input(" Please take your move, select an empty space for X : "))
            if player1_move==board[0]:
                print("\nSorry, that\'s not a valid move. Try again! ")
                time.sleep(1)
                error = 1
            elif board[player1_move] == "-":        #Check the move is available or not
                board[player1_move] = "X"
                error = 0
            else:
                print("\nSorry, that\'s not a valid move. Try again! ")
                time.sleep(1)
                error = 1
        except ValueError:                          #Ask for take a move again if the input is not a number
            print("\nSorry, that\'s not a valid move. Try again! ")
            time.sleep(1)
        except IndexError:
            print("\nSorry, that\'s not a valid move. Try again! ")
            time.sleep(1)
        os.system('clear')
        print_board(board)
    
        
#Define the player O moves
def player2_move():   
    error = 1
    while error == 1:
        try:
            player2_move = int(input(" Please take your move, select an empty space for O : "))
            if player2_move==board[0]:
                print("\nSorry, that\'s not a valid move. Try again! ")
                time.sleep(1)
                player2_move()
                error = 1
            elif board[player2_move] == "-":    #Check the move is available or not
                board[player2_move] = "O"
                error = 0
            else:
                print("\nSorry, that\'s not a valid move. Try again! ")
                time.sleep(1)
                error = 1
        except ValueError:                      #Ask for take a move again if the input is not a number
            print("\nThat's not a number. Try again")
            time.sleep(1)
        except IndexError:
            print("\nSorry, that\'s not a valid move. Try again! ")
            time.sleep(1)
        os.system('clear')
        print_board(board)

    
#Select which player starts
def player_select(rp): 
    rp = random.randint(0,1)
    if rp == 0:
        print('Player X will start the game')
        return rp
    else:
        print('Player O will start the game')
        return rp
        

#Check winner rules
#Check winner X
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

#Check winner O
def check_win(O):
    if (board[7] == O and board[8] == O and board[9] == O) or \
        (board[4] == O and board[5] == O and board[6] == O) or \
        (board[1] == O and board[2] == O and board[3] == O) or \
        (board[7] == O and board[4] == O and board[1] == O) or \
        (board[8] == O and board[5] == O and board[2] == O) or \
        (board[9] == O and board[6] == O and board[3] == O) or \
        (board[7] == O and board[5] == O and board[3] == O) or \
        (board[9] == O and board[5] == O and board[1] == O):
        return True
    else:
        False

#Ask the player for a new game
def endofgame():
    newgame = input("Would you like to challange somebody again? Y or N? : ")
    if  newgame == "Y" or newgame == "y":
            board[0]='-'
            board[1]='-'
            board[2]='-'
            board[3]='-'
            board[4]='-'
            board[5]='-'
            board[6]='-'
            board[7]='-'
            board[8]='-'
            board[9]='-'
            os.system('clear')
            print_board(board)
            print("Random selecting player...")
            time.sleep(2)
            main()
    elif newgame == "N" or newgame == "n":
            print("What\'s wrong? CHICKEN??")
            time.sleep(2)
            quit()
    else:
        endofgame()


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

                            **Press Enter to randomly select the Starting Player!**
    """
    print(header)
    input()


def main():
    os.system('clear')
    print_board(board)
    rp = random.randint(0,1)                #Select which player starts
    if rp == 0:
        print('Player X will start the game')
    else:
        print('Player O will start the game')
    turn = 0
    while turn < 9:
        if rp == 0:
            rp+=1
            player1_move()
            turn += 1
            if check_win('X') == True:      #Check for X win
                os.system('clear')
                print_board(board)
                print("Congratulations! Player X won!")
                endofgame()
        else:
            rp -= 1
            player2_move()
            turn +=1
            if check_win('O') == True:      #Check for O win
                os.system('clear')
                print_board(board)
                print("Congratulations! Player O won!")
                endofgame()
    else:
        print( "The game is a TIE.")
        endofgame()

print_header()
main()