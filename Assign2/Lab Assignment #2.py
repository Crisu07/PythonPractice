# Lab Assignment 2
# 09/20/19

# Variables
tip_only = 0
tips = 0.18

tax_only = 0
taxes = 0.07

meal_price_only = 0
total_meal_price = 0

# User inputs the price of the meal
meal_price_only = float(input("Please enter the price of the meal: "))
# Display price of the meal entered to make sure
print("The price of the meal is ", meal_price_only)

# Calculation of the amount of tips to pay from 18%
tip_only = meal_price_only * tips
print("The total amount of tip to pay is ", tip_only)

# Calculation of the amount of tax to pay from 7%
tax_only = meal_price_only * taxes
print("The total amount of tax is ", tax_only)


# Calculation of the final restuarant meal with the tax and tip
total_meal_price = meal_price_only + tip_only + tax_only
print("The total restuarant bill is ", total_meal_price)


====== RESTART: C:/Users/chris/Desktop/Python 3.7/Lab Assignment #2.py ======
Please enter the price of the meal: 20.00
The price of the meal is  20.0
The total amount of tip to pay is  3.5999999999999996
The total amount of tax is  1.4000000000000001
The total restuarant bill is  25.0
>>> 
