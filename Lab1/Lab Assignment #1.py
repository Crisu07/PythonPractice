# Lab Assignment #1
# Due 02/03/20

height = float(input('Please enter your height in inches: '))
weight = float(input('Please enter your weight in pounds: '))

BMI = float((weight * 703)/(height * height))
print(format(BMI, '.2f'))
