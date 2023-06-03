# Lab Assignment #2 part 2
# Due 02/05/20

import random

print('This is lab 2-2')

# Loop to roll the dice 3 times total
for x in range(3):
    dice_value = random.randint(1, 6)
    print('The value of the dice is', dice_value)
