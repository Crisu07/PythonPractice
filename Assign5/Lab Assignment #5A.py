# Lab Assignment 5A
# 10/04/19

# ask user to enter two numbers
# add the two numbers and display
# ask user if they want to perform the action again
# if yes, repeat loop or else terminate

total = 0

number1 = int(input("Please enter a number: "))
number2 = int(input("Please enter another number: "))

total = number1 + number2
print("The sum of the two numbers is,", total)

# Ask user if they want to repeat
print("Enter 1 for yes and 2 for no")
question = int(input("Do you want to perform this operation again?: "))

# Loop
while question == 1:
    number1 = int(input("Please enter a number: "))
    number2 = int(input("Please enter another number: "))
    total = number1 + number2
    
    print("The sum of the two numbers is,", total)
    print("Enter 1 for yes and 2 for no")
    
    question = int(input("Do you want to perform this operation again?: "))


>>> 
====== RESTART: C:\Users\chris\Desktop\Python 3.7\Lab Assignment #5A.py ======
Please enter a number: 6
Please enter another number: 9
The sum of the two numbers is, 15
Enter 1 for yes and 2 for no
Do you want to perform this operation again?: 1
Please enter a number: 5
Please enter another number: 8
The sum of the two numbers is, 13
Enter 1 for yes and 2 for no
Do you want to perform this operation again?: 1
Please enter a number: 49
Please enter another number: 126
The sum of the two numbers is, 175
Enter 1 for yes and 2 for no
Do you want to perform this operation again?: 2
>>> 
