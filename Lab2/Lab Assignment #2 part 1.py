# Chris Nguyen
# 025513031
# CECS 174 Section 05
# Lab Assignment #2 Part 1
# Due 02/05/20

loan = float(input('Please enter the amount of the loan: '))
months = int(input('Please enter the number of months for the loan: '))
interest = float(input('Please enter the annual interest rate: '))

month_payment = (interest/12)*loan / (1-(1+(interest/12))**-months)

print("The amount of the monthly payment is $", format(month_payment, '.2f'))
