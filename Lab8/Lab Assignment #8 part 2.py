# Lab Assignment 8 part 2
# Due 4/11/20

def main():
    board = [' ',' ',' ',
             ' ',' ',' ',
             ' ',' ',' ']

    thegame(board)
    

def drawboard(board):
# organizes the game board
    print('-------------')
    print('|', board[0], '|', board[1], '|', board[2], '|')
    print('-------------')
    print('|', board[3], '|', board[4], '|', board[5], '|')
    print('-------------')
    print('|', board[6], '|', board[7], '|', board[8], '|')
    print('-------------')

def thegame(board):
    turn = 'X'
    count = 0

    # Range 10 because maximum of 9 moves only
    for n in range(10):
        drawboard(board)
        print('It is', turn,"'s turn.")
        row = int(input('Please enter a row number (1-3):'))
        column = int(input('Please enter a column number (1-3):'))

        # Marks the board with the space that the player has chosen
        if row == 1 and column == 1:
            board[0] = turn
            count += 1
        elif row == 1 and column == 2:
            board[1] = turn
            count += 1
        elif row == 1 and column == 3:
            board[2] = turn
            count += 1
        elif row == 2 and column == 1:
            board[3] = turn
            count += 1
        elif row == 2 and column == 2:
            board[4] = turn
            count += 1
        elif row == 2 and column == 3:
            board[5] = turn
            count += 1
        elif row == 3 and column == 1:
            board[6] = turn
            count += 1
        elif row == 3 and column == 2:
            board[7] = turn
            count += 1
        elif row == 3 and column == 3:
            board[8] = turn
            count += 1

        # Check to see if any player won for every move after 5 moves
        if count >= 5:
            # Check for 3 in a rowacross top row and ignore if same blanks
            if board[0] == board[1] == board[2]!= ' ':
                drawboard(board)
                print('Player', turn, 'is the winner')
                break
            # Checks across the middle row
            elif board[3] == board[4] == board[5] != ' ':
                drawboard(board)
                print('Player', turn, 'is the winner')
                break
            # Checks across the bottom row
            elif board[6] == board[7] == board[8] != ' ':
                drawboard(board)
                print('Player', turn, 'is the winner')
                break
            # Checks down the left side
            elif board[0] == board[3] == board[6] != ' ':
                drawboard(board)
                print('Player', turn, 'is the winner')
                break
            # Checks down the middle side
            elif board[1] == board[4] == board[7] != ' ':
                drawboard(board)
                print('Player', turn, 'is the winner')
                break
            # Checks down the right side
            elif board[2] == board[5] == board[8] != ' ':
                drawboard(board)
                print('Player', turn, 'is the winner')
                break
            # Checks diagonals
            elif board[0] == board[4] == board[8] != ' ':
                drawboard(board)
                print('Player', turn, 'is the winner')
                break
            elif board[2] == board[4] == board[6] != ' ':
                drawboard(board)
                print('Player', turn, 'is the winner')
                break
            elif count == 9:
                drawboard(board)
                print('It is a tie')
                break
                
        # Changes to the next player's mark
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

        
    
main()

