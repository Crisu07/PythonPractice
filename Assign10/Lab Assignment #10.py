# Lab Assignment #10
# 10/25/19

# word for word on the display prints even the period
# do not ask user to quit, automatically generate a new number (keeps going)
# must use one main function and atleast TWO addition functions


import random

def main():

    number = random.randint(1,10)

    user_input = 0
    
    count = 0
    
    while user_input != number:

# Asks user to guess a number between the range
        user_input = user1()

# If the guess is too high
        if user_input < number:
            message()
            count += 1

# If the guess is too low
        elif user_input > number:
            message2()
            count += 1

# If the guess is correct
        else:
            print("Congratulations!!!")
            count += 1
            print("You took", count, "attempt(s) to get it right")

    main()


def user1():

    user_input = int(input("Guess a number between 1 and 10: "))
    return user_input

def message():
    print("Too low, try again.")

def message2():
    print("Too high, try again.")
    
main()

