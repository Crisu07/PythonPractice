# Chris Nguyen
# 025513031
# CECS 174 Section 05
# Lab Assignment #3 part 2
# Due 02/17/20

#                             Psuedocode
# explain the rules of the game to player
# rolls dice for the player and display the results
# rolls dice for the computer and display results
# compare both results
# display who the winner is or if it was a tie

def main():

    import random
# Calculating the rolls of the player
    roll = random.randint(1,6)
    roll2 = random.randint(1,6)

# Calculating the rolls of the computer
    roll3 = random.randint(1,6)
    roll4 = random.randint(1,6)

# Checks to see if the rolls had the same face
    face = 0
    if roll == roll2:
        print('You rolled both a', roll, 'and a', roll2)
        face = 1
    else:
        print('You rolled a', roll, 'and a', roll2)

    face2 = 0
    if roll3 == roll4:
        print('The computer rolled both a', roll3, 'and a', roll4)
        face2 = 1
    else:
        print('The computer rolled a', roll3, 'and a', roll4)

# Calculate the total of the rolls
    dice_sum1 = roll + roll2
    dice_sum2 = roll3 + roll4

# Comparisons of results
    if face > 0 and face2 > 0:
        if dice_sum1 > dice_sum2:
            print('You have the higher roll. You win!')
        elif dice_sum1 < dice_sum2:
            print('The computer has the higher roll. You lost!')
        else:
            print('It is a tie!')
    elif face == 0 and face2 == 0:
        if dice_sum1 > dice_sum2:
            print('You have the higher roll. You win!')
        elif dice_sum1 < dice_sum2:
            print('The computer has the higher roll. You lost!')
        else:
            print('It is a tie!')
    elif face == 1 and face2 != 1:
        print("You rolled the same face and the computer didn't. You win!")
    elif face != 1 and face2 == 1:
        print("The computer rolled the same face and you didn't. You lose!")

main()
