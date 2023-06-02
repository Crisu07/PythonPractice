# Chris Nguyen
# 025513031
# CECS 174 Section 05
# Lab Assignment #6 part 1
# Due 3/9/20

def main():
    print('Please enter a total of 15 numbers')
    numbers = []
# Repeats 15 times for user to enter all values
    for x in range(15):
        user_input = int(input('Please enter a number:'))
# Creates list of the inputted numbers
        numbers.append(user_input)
        
    display_stats(numbers)

def display_stats(numbers):

# Calculating minimum value of the inputted numbers
    current_min = numbers[0]
    for x in numbers:
        if x < current_min:
            current_min = x
    print('The minimum value is', current_min)

# Calculating maximum value of the inputted numbers
    current_max = numbers[0]
    for x in numbers:
        if x > current_max:
            current_max = x
    print('The maximum value is', current_max)

# Calculating the average value
    total_sum = 0
    for x in numbers:
        total_sum += x
    total_sum /= 15
    print('The average value is', format(total_sum, '.1f'))
        

main()
