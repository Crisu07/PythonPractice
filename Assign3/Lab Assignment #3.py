# Lab Assignment 3
# 09/20/19

# Variables
one = "Monday"
two = "Tuesday"
three = "Wednesday"
four = "Thursday"
five = "Friday"
six = "Saturday"
seven = "Sunday"

user_input = 0

# Prompts user to input a number between 1 and 7
user_input = int(input("Please enter a nondecimal number between 1 and 7: "))
print("The number you entered was", user_input)

# Answers based on if the user enters between the number range
if user_input == 1:
    print("The corresponding day to 1 is", one)

if user_input == 2:
    print("The corresponding day to 2 is", two)

if user_input == 3:
    print("The corresponding day to 3 is", three)

if user_input == 4:
    print("The corresponding day to 4 is", four)

if user_input == 5:
    print("The corresponding day to 5 is", five)

if user_input == 6:
    print("The corresponding day to 6 is", six)

if user_input == 7:
    print("The corresponding day to 7 is", seven)

# If the user inputs a number outside of the required number range
if user_input < 1:
    print("This is outside of the number range, please try again")

if user_input > 7:
    print("This is outside of the number range, please try again")


# SUPPOSED TO TEST IT FOR ALL INPUTS NOT JUST ONE, MISSED SOME POINTS 
====== RESTART: C:/Users/chris/Desktop/Python 3.7/Lab Assignment #3.py ======
Please enter a nondecimal number between 1 and 7: 6
The number you entered was 6
The corresponding day to 6 is Saturday
>>> 
====== RESTART: C:/Users/chris/Desktop/Python 3.7/Lab Assignment #3.py ======
Please enter a nondecimal number between 1 and 7: 8
The number you entered was 8
This is outside of the number range, please try again
>>> 
