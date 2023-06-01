# Lab Assignment #7
# 10/18/19

# Variables
state_tax = 0.05
county_tax = 0.025
purchase = 0
total_sales_tax = 0
sales_total = 0
state_total = 0
county_total = 0

def main():

    purchase = main2()
    
    state_total = purchase * 0.05
    print("The state sales tax is", '$', format(state_total, '.2f'))
    
    county_total = purchase * 0.025
    print("The county sales tax is", '$', format(county_total, '.2f'))
    
    total_sales_tax = state_total + county_total
    print("The total sales tax is", '$', format(total_sales_tax, '.2f'))
    
    sales_total = purchase + total_sales_tax
    print("The total sales purchase is", '$', format(sales_total, '.2f'))

def main2():
    purchase = float(input("Please enter the amount of your purchase: "))
    print("The amount of the purchase is", '$', format(purchase, '.2f'))
    return purchase

main()

>>> 
====== RESTART: C:\Users\chris\Desktop\Python 3.7\Lab Assignment #7.py ======
Please enter the amount of your purchase: 134.98
The amount of the purchase is $ 134.98
The state sales tax is $ 6.75
The county sales tax is $ 3.37
The total sales tax is $ 10.12
The total sales purchase is $ 145.10
>>> 
====== RESTART: C:\Users\chris\Desktop\Python 3.7\Lab Assignment #7.py ======
Please enter the amount of your purchase: 253.45
The amount of the purchase is $ 253.45
The state sales tax is $ 12.67
The county sales tax is $ 6.34
The total sales tax is $ 19.01
The total sales purchase is $ 272.46
>>> 
