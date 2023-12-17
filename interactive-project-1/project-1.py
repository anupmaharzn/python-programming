# create a tic tac toe game for 2 human players
"""
game and approach

2 players should be able to play the game (both sitting at the same computer)

the board should be printed out every time a player makes a move

you should be able to accept input of he player position and then place a symbol on the board

"""


#step 1 would be to write a function that can print out a board

def display_board(board):
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])


#step 2 would be to write a function that can take in a player input and assign their marker as 'X or 'O

def player_input():
    """
    output=(player1 marker ,player 2 marker)
    """
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player1:Choose X or O: ').upper()

    if marker == 'X':

        return ('X','O')
    else:
        return ('O','X')
    


#step 3 is to write a function that takes in the board list object, a marker ('X' or 'O') and a desired position (number 1-9) and assigns it to the board.

def place_marker(board,marker,position):

    board[position] = marker



#step 4 write a function that takes in a board and a mark ( X or O) and then checks to see if that marks has won.

def win_check(board,mark):

    # win tic tac toe?
    #all rows, and check to see if they all share the same marker?
    # all columns , check to see if marker matches
    # 2 diagnoals,check to see match
    return (
    (board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[1] == mark and board[4] == mark and board[7] == mark) or
    (board[2] == mark and board[5] == mark and board[8] == mark) or
    (board[3] == mark and board[6] == mark and board[9] == mark) or
    (board[1] == mark and board[5] == mark and board[9] == mark) or
    (board[3] == mark and board[5] == mark and board[7] == mark)
    )



# step 5 waf that uses the random module to randomly decide which player goes first.

import random

def choose_first():
    
    flip = random.randint(0,1)
    
    if flip == 0:
        return 'Player 1'

    else:
        return 'Player 2'

# step 6 waf that returns a boolean indicating wheather a space on the board is freelly available

def space_check(board,position):

    return board[position] == ' '

# step 7 waf that checks if the board is full and retuns a boolean value .true if full,false otherwise

def full_board_check(board):

    for i in range(1,10):
        if space_check(board,i):
            return False
    #board is full if we return true
    return True

#step 8 waf that asks for a player's next position(as a number 1-9) and then uses the function from step 6 to check if it's a free position.if it is ,then return the position for later use.

def player_choice(board):

    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('choose a position: (1-9)'))

    return position

#step 9 waf that asks the player if they want to play again and returns a boolean true if they do want to play again

def replay():

    choice = input("Play again? Enter Yes or No")

    return choice == 'Yes'


#step 10 here comes the hard part , use while loops and the fucntion we have made to run game


#while loop to keep running the game
print('wlcome to tic tac toe')

while True:

    #play the game 

    ## set everything up (board,who first,choose marker x,o )
     
    the_board = [' '] * 10 #output [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    player1_marker,player2_marker = player_input()

    turn = choose_first()
    print(turn + 'will go first')

    play_game = input('Ready to play? y or n')

    if play_game == 'y':
        game_on = True
    else:
        game_on = False
    ## game play

    while game_on:
        if turn == 'Player 1':

            #show the board
            display_board(the_board)
            #choose a position

            position = player_choice(the_board)
            #place the marker onthe position
            place_marker(the_board,player1_marker,position)

            #check if they won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('Player 1 has won')
                game_on = False

            # or check if there is a tie
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie game!')
                    game_on =False
                else:
                    # no tie and no win? then next player's turn
                    turn='Player 2'

        else:
            #show the board
            display_board(the_board)
            #choose a position

            position = player_choice(the_board)
            #place the marker onthe position
            place_marker(the_board,player2_marker,position)

            #check if they won
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('Player 2 has won')
                game_on = False

            # or check if there is a tie
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie game!')
                    game_on =False
                else:
                    # no tie and no win? then next player's turn
                    turn='Player 1'
            
# break out of the while loop on replay() 
    if not replay():
        break



