# Lab Assignment 1
# 09/20/19

print("This is a lab program")

# Variables
tax_only = 0
# Percentage of taxes as a rate
taxes = 0.0925
# Cost of the items without the tax included
total_items_price = 0
# Total cost of items including tax
total_purchase_price = 0

item1 = float(input("Please enter the price of the first item: "))
item2 = float(input("Please enter the price of the second item: "))
item3 = float(input("Please enter the price of the third item: "))
item4 = float(input("Please enter the price of the fourth item: "))
item5 = float(input("Please enter the price of the fifth item: "))

total_items_price = item1 + item2 + item3 + item4 + item5
print("The cost of all the items is ", total_items_price)

tax_only = total_items_price * taxes
print("The total tax cost is ", tax_only)

total_purchase_price = total_items_price + tax_only
print("The total amount of your purchase is ", total_purchase_price)


====== RESTART: C:/Users/chris/Desktop/Python 3.7/Lab Assignment #1.py ======
This is a lab program
Please enter the price of the first item: 4.25
Please enter the price of the second item: 3.75
Please enter the price of the third item: 3.50
Please enter the price of the fourth item: 2.00
Please enter the price of the fifth item: 5.75
The cost of all the items is  19.25
The total tax cost is  1.780625
The total amount of your purchase is  21.030625
>>> 
