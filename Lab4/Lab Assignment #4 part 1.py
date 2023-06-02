# Chris Nguyen
# 025513031
# CECS 174 Section #5
# Lab Assignment #4 part 1
# Due 02/19/20

#                       Pseudocode
# ask for input of BMI of multiple people
# will ask for the user height in inches and weight in pounds each time
# take that amount and calculate the BMI index
# display the weight status of the person
# ask user if they want to use the BMI calculator again
# repeat if yes and end if no
# test output at least 5 times

def main():
    print('Welcome to BMI calculator')

# Asks user to enter height and weight
    height = float(input('Please enter the height in inches:'))
    weight = float(input('Please enter the weight in lbs:'))

# Calculates the BMI 
    BMI = float((weight * 703)/(height**2))
    print('BMI Index is:', format(BMI, '.2f'))

# Check to see what to display based on BMI
    if BMI < 18.5:
        print('The weight status is UNDERWEIGHT')
    elif BMI >= 18.5 and BMI <= 24.9:
        print('The weight status is NORMAL / HEALTHY')
    elif BMI >= 25.0 and BMI <= 29.9:
        print('The weight status is OVERWEIGHT')
    else:
        print('The weight status is OBESE')

main()

# Loop to repeat the BMI Calculator again
reply = 'y'
while reply in ('Y','y'):
    reply = input('Would you like to process one more case(Y/N or y/n)?')
    if reply == 'y' or reply == 'Y':
        main()
    else:
        print('Thank you for using BMI Calculator - Have a good day!')
