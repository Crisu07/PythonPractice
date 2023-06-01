# Lab Assignment #8
# 10/18/19

# must use at least one main function and atleast 2 other functions
# square feet entered should NOT be a multiple of 92
# should test multiple outputs

# Variables
square_feet = 0
paint_gallons = 0
hours = 0
labor_charges = 0
gallon_cost = 0
paint_cost = 0
total_cost = 0

def main():

    square_feet = user1()

    gallon_cost = user2()
    
    paint_gallons = square_feet/92
    print("The number of gallons of paint required is", paint_gallons)
    
    hours = ((square_feet / 92) * 8)
    print("The hours of labor required is", hours)

    paint_cost = paint_gallons * gallon_cost
    print("The cost of the paint is $", format(paint_cost, '.2f'))
    
    labor_charges = hours * 30.00
    print("The labor charge is", '$', format(labor_charges, '.2f'))

    total_cost = labor_charges + paint_cost
    print("The total cost of the paint job is $", format(total_cost,'.2f'))


def user1():
    square_feet = int(input("Enter the square feet of wall space to paint: "))
    print("The amount of square feet entered is", square_feet)
    return square_feet

def user2():
    gallon_cost = float(input("Enter price of one gallon of paint: $"))
    return gallon_cost

main()

>>> 
====== RESTART: C:\Users\chris\Desktop\Python 3.7\Lab Assignment #8.py ======
Enter the square feet of wall space to paint: 186
The amount of square feet entered is 186
Enter price of one gallon of paint: $5.36
The number of gallons of paint required is 2.0217391304347827
The hours of labor required is 16.17391304347826
The cost of the paint is $ 10.84
The labor charge is $ 485.22
The total cost of the paint job is $ 496.05
>>> 
====== RESTART: C:\Users\chris\Desktop\Python 3.7\Lab Assignment #8.py ======
Enter the square feet of wall space to paint: 274
The amount of square feet entered is 274
Enter price of one gallon of paint: $9.28
The number of gallons of paint required is 2.9782608695652173
The hours of labor required is 23.82608695652174
The cost of the paint is $ 27.64
The labor charge is $ 714.78
The total cost of the paint job is $ 742.42
>>> 

