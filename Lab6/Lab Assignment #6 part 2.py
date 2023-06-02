# Chris Nguyen
# 025513031
# CECS 174 Section 05
# Lab Assignment #6 part 2
# Due 3/9/20

# Worked on algorithm with Mikaela Posada

#                              Pseudocode
# create main function that will include and call the following
# 
# create accept_input function
#   should ask user to input a year
#   call leap year verifying function
#   repeat until user enters 0 to stop
#   
# create leap_year_verifier function
#   this function will check if year inputted is a leap year
#   if user input is divisible by 4 and not 100 or completely
#   divisible by 400 then it is a leap year
#   call the display function to display results
#
# create display_output function
#   displays the result
#   display whether or not the inputted year was a leap year or not

def main():
    print('Welcome to Leap Year Verifier. \n')
    year = 1
    while year != 0:
# Calls input function
        year = accept_input()
# Calls the verifying function
        leap_year_verifier(year)
    else:
        print('Thank You for using the Leap Year Verifier.')
    
def accept_input():
# Asks user to enter a year greater than 1582
    ans = int(input('Please enter a year that is 1582 or later,(0 to stop):'))
    return ans

def leap_year_verifier(year):
    leap_year = 0
# Calculates and checks if the entered year was a leap year
    if ((year%4 == 0 and year%100 != 0) or year%400 == 0) and leap_year != year:
        leap_year += 1
# Calls display function
    display_output(leap_year, year)

def display_output(leap_year, year):
    if leap_year == 1:
        print(year, 'is a leap year. \n')
    elif leap_year == 0 and year == 0:
        year = 0
        return year
    else:
        print(year, 'is not a leap year. \n')

main()
