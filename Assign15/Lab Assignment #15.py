# Lab Assignment #15
# 11/22/19


def main():

# Variables
    index = 0
    total = 0
    average = 0
    
# List
    series = [0] * 10

    for index in range(10):
        series[index] = int(input("Enter a number: "))
        index += 1
# Display
    print(series)
    print("The highest value of the list is:", max(series))
    print("The lowest value of the list is:", min(series))
    
# Calculating total of numbers in list
    for n in series:
        total += n
    print("The total of the numbers in the list is:", total)


    average = total/len(series)
    print("The average of the numbers in the list is:", average)
    

main()

# >>> 
# ====== RESTART: C:\Users\chris\Desktop\Python 3.7\Lab Assignment #15.py ======
# Enter a number: 12
# Enter a number: 45
# Enter a number: 16
# Enter a number: 39
# Enter a number: 71
# Enter a number: 24
# Enter a number: 13
# Enter a number: 02
# Enter a number: 94
# Enter a number: 16
# [12, 45, 16, 39, 71, 24, 13, 2, 94, 16]
# The highest value of the list is: 94
# The lowest value of the list is: 2
# The total of the numbers in the list is: 332
# The average of the numbers in the list is: 33.2
# >>>

# >>> 
# ====== RESTART: C:\Users\chris\Desktop\Python 3.7\Lab Assignment #15.py ======
# Enter a number: 5
# Enter a number: 25
# Enter a number: 84
# Enter a number: 69
# Enter a number: 12
# Enter a number: 03
# Enter a number: 96
# Enter a number: 47
# Enter a number: 59
# Enter a number: 71
# [5, 25, 84, 69, 12, 3, 96, 47, 59, 71]
# The highest value of the list is: 96
# The lowest value of the list is: 3
# The total of the numbers in the list is: 471
# The average of the numbers in the list is: 47.1
# >>> 
