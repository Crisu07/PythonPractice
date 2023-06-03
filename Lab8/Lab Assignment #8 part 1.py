# Lab Assignment 8 part 1
# Due 4/11/20

#                              Pseudocode
# Create a list that depicts the functions of the board
# Create a function that breaks the list up and turns it into
# an actual tic tac toe board and displays
# Create a function that checks winning cases of the game
#   check for same marks going across and diagonally
#   disregard if blank marks were involved
#   display results of whether play X or O won or lost
# Assign values to the board by corresponding marks with the indexes
# in the list

def main():
    # Change values to check outcomes
    board = ['O','X','O',
             'X','O','O',
             'X','X','X']

    drawboard(board)
    # Change player to check values
    player = 'X'

    is_winner(board, player)
    
def drawboard(board):
# organizes the game board
    print('-------------')
    print('|', board[0], '|', board[1], '|', board[2], '|')
    print('-------------')
    print('|', board[3], '|', board[4], '|', board[5], '|')
    print('-------------')
    print('|', board[6], '|', board[7], '|', board[8], '|')
    print('-------------')

def is_winner(board, player):
  # Check for 3 in a rowacross top row and ignore if same blanks
    if board[0] == board[1] == board[2] == player != ' ':
        print('Player', player, 'is the winner')
        
    # Checks across the middle row
    elif board[3] == board[4] == board[5] == player != ' ':
        print('Player', player, 'is the winner')
        
    # Checks across the bottom row
    elif board[6] == board[7] == board[8] == player != ' ':
        print('Player', player, 'is the winner')
        
    # Checks down the left side
    elif board[0] == board[3] == board[6] == player != ' ':
        print('Player', player, 'is the winner')
        
    # Checks down the middle side
    elif board[1] == board[4] == board[7] == player != ' ':
        print('Player', player, 'is the winner')
        
    # Checks down the right side
    elif board[2] == board[5] == board[8] == player != ' ':
         print('Player', player, 'is the winner')
         
    # Checks diagonals
    elif board[0] == board[4] == board[8] == player != ' ':
         print('Player', player, 'is the winner')
         
    elif board[2] == board[4] == board[6] == player != ' ':
         print('Player', player, 'is the winner')

    else:
         print('Player', player, 'did not win')


main()
