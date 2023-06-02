# Chris Nguyen
# 025513031
# CECS 174 Section 05
# Lab Assignment #3 part 1
# Due 02/17/20

#         Pseudocode
# ask user for input of how many guitars they are buying
# if it is between 10-19 guitars then it will be a 10% discount
# if 20-49 then 20%, 50-99 then 30%, and if over 100 than 40%
# calculate the discounted price with the corresponding percentage discount
# calculate total price that the buyer will have to pay

amount = 0
total = 0
guitars = int(input('Enter the quantity of guitars that you will be buying: '))

if guitars >= 10 and guitars <=19:
    amount = (100 * (1 - .1))
    total = amount * guitars
    
elif guitars >= 20 and guitars <=49:
    amount = (100 * (1 - .2))
    total = amount * guitars
    
elif guitars >= 50 and guitars <= 99:
    amount = (100 * (1 - .3))
    total = amount * guitars
    
elif guitars >= 100:
    amount = (100 * (1 - .4))
    total = amount * guitars

else:
    amount = float(guitars * 100)
    total = amount

print('The total price for these guitars would be:$', format(total, '.2f'))
