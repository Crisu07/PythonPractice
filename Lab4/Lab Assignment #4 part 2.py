# Chris Nguyen
# 025513031
# CECS 174 Section #5
# Lab Assignment #4 part 2
# Due 02/19/20

#                        Pseudocode
# Ask player to enter the amount of money they have
# Ask user to input how much they want to bet
# rolls dice for the player and display results
# rolls dice for the computer and display results
# compare both results
# check to see if they rolled same faces
# display the results: win loss or tie
# subtract costs of bet from total if it was a loss
# leave it if it was a tie
# add the bet amount to total if it was a win
# ask user if they want to play again or quit
# will automatically quit if user runs out of money

# User enter money
money = float(input('Please enter the amount of money you have:'))

# will repeat if user wants to continue playing
answer = 'y'
while answer in ('y', 'Y'):
    bet = float(input('How much would you like to bet?'))

# Will not run if user bets more than what they have
    if bet > money:
        print('You can not bet more than what you have')
        answer = input('Do you want to try again?(y/n or Y/N)')
    else:
# Dice game and calculations
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

    # Comparisons of results and adjusting money depending on bets won/loss
        if face > 0 and face2 > 0:
            if dice_sum1 > dice_sum2:
                print('You have the higher roll. You win!')
                money += bet
            elif dice_sum1 < dice_sum2:
                print('The computer has the higher roll. You lost!')
                money -= bet
            else:
                print('It is a tie!')
        elif face == 0 and face2 == 0:
            if dice_sum1 > dice_sum2:
                print('You have the higher roll. You win!')
                money += bet
            elif dice_sum1 < dice_sum2:
                print('The computer has the higher roll. You lost!')
                money -= bet
            else:
                print('It is a tie!')
        elif face == 1 and face2 != 1:
            print("You rolled the same face and the computer didn't. You win!")
            money += bet
        elif face != 1 and face2 == 1:
            print("The computer rolled the same face and you didn't. You lose!")
            money -= bet
        print('You have a total of', money, 'left')
        answer = input('Do you want to play again?(y/n or Y/N)')

print('You have a total of', money, 'left')
    

