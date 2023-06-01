# Lab Assingment #14
# 11/15/19

import random

def main():

# Creating the original list
    lottery = [0] * 7

    index = 0

# Loop that generates a random number to add to each index of the list
    while index < len(lottery):
        number = random.randint(0,9)
        lottery[index] = number
        index += 1

# Loop that displays the numbers within the range of the lottery numbers
    for index in range(len(lottery)):
        print(lottery[index])


main()

# >>> 
# ====== RESTART: C:\Users\chris\Desktop\Python 3.7\Lab Assignment #14.py ======
# 1
# 0
# 4
# 3
# 7
# 3
# 8
# >>> 
# ====== RESTART: C:\Users\chris\Desktop\Python 3.7\Lab Assignment #14.py ======
# 2
# 1
# 5
# 5
# 0
# 8
# 9
# >>> 
# ====== RESTART: C:\Users\chris\Desktop\Python 3.7\Lab Assignment #14.py ======
# 1
# 7
# 8
# 5
# 8
# 1
# 8
# >>> 
