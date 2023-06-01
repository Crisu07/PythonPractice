# Lab Assignment #13
# 11/15/19

def main():

# Variables
    index = 0
    index2 = 0
    sales_total = 0
    sales = 0

# Lists
    list1 = [0] * 5
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

# Calculating inputs of the sales earned each day
    while index < len(list1):
        print("On", days[index2])
        list1[index] = float(input("enter sales earned this day: $")) 
        index += 1
        index2 += 1

# Loop to Calculate the total sales
    for sales in list1:
        sales_total += sales

    print("The total sales earned was $", format(sales_total, '.2f'))


main()

# >>> 
# ====== RESTART: C:\Users\chris\Desktop\Python 3.7\Lab Assignment #13.py ======
# On Monday
# enter sales earned this day: $42.36
# On Tuesday
# enter sales earned this day: $78.93
# On Wednesday
# enter sales earned this day: $52.18
# On Thursday
# enter sales earned this day: $72.46
# On Friday
# enter sales earned this day: $37.57
# The total sales earned was $ 283.50
# >>> 
# ====== RESTART: C:\Users\chris\Desktop\Python 3.7\Lab Assignment #13.py ======
# On Monday
# enter sales earned this day: $86
# On Tuesday
# enter sales earned this day: $95
# On Wednesday
# enter sales earned this day: $25
# On Thursday
# enter sales earned this day: $74
# On Friday
# enter sales earned this day: $31
# The total sales earned was $ 311.00
# >>> 
