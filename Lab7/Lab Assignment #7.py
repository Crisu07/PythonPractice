# Lab Assignment 7
# Due 3/18/20

#                           Pseudocode
# Create main function
    # Create the two tracks for hare and tortoise in form of list
    # call functions that create index number
# create function that creates random index number
    # use random function to call an index
    # use numbers 1-10 in a tuple to identify the percentage of the move
    # add that mvoe to the current index
    # make sure index values are between 0 and 69 only
    # create one of these each for rabbit and turtle
# return the index values to the main function
# Replace the specific index value of the track with R or T depending on which
# Convert list to a string and display the race (could make this a function)
# Loop main until either T or R gets to index 69
    # Determine current index of each animal
    # Pass current indexes into main function
    # create a tracker for the index
# Loop will break once one or both animals reach index 69
# Display results of who won or whether it was a tie

import random

def main(a, b):
    t_index = a
    r_index = b
    
    t_squares = '-'
    t_spaces = []
    for x in range(70):
        t_spaces.append(t_squares)

    r_squares = '-'
    r_spaces = []
    for x in range(70):
        r_spaces.append(r_squares)

    a = tortoise(t_index)
    b = rabbit(r_index)
# Index starts at 0 so add 1 for technically the correct track mark
    print('Tortoise postion:', a + 1, ', Hare position:', b + 1)
    
    t_spaces[a] = 'T'

    r_spaces[b] = 'R'

    list2string(t_spaces)

    list2string(r_spaces)

    return a, b
    
def tortoise(t_index):
    t = t_index
    t_movetype = (1,2,3,4,5,6,7,8,9,10)
    t_move = random.randint(1,10)

# Checks for fast plod 50% of time
    if t_move <= 5:
       t += 3
# Checks for slip 20% of time
    elif t_move == 6 or t_move == 7:
        t -= 6
# Checks for slow plod 30% of time
    else:
        t += 1
# Make sure it does not slip lower than mark 1 or higher than mark 70
    if t < 0:
        t = 0
    elif t >= 69:
        t = 69
    return t

def rabbit(r_index):
    r = r_index
    r_movetype = [1,2,3,4,5,6,7,8,9,10]
    r_move = random.randint(1,10)

# Checks for sleep 20% of time
    if r_move <= 2:
        r += 0
# Check for big hop 20% of time
    elif r_move == 3 or r_move == 4:
        r += 9
# Checks for big slip 10% of time
    elif r_move == 5:
        r -= 12
# Checks for small hop 30% of time
    elif r_move == 6 or r_move == 7 or r_move == 8:
        r += 1
# Checks for small slip 20% of time
    else:
        r -= 2
# Makes sure it does not slip lower than mark 1 or higher than mark 70
    if r < 0:
        r = 0
    elif r >= 69:
        r = 69
    return r

def list2string(s):
    str1 = ''
    for x in s:
        str1 += x
    print(str1)

a = 0
b = 0

# Loop until one finishes the race
while a >= 0 and b >= 0:
    x,y = main(a,b)
    a = x
    b = y
    if a >= 69:
        print('Tortoise won!')
        break
    elif b >= 69:
        print('Hare won!')
        break
    elif a >= 69 and b >= 69:
        print('It\'s a tie')
        break
    
