# Lab Assignment #15 EC
# 11/22/19

import random

def main():
    
# Variables
    n = 0
    index = 0
    index2 = 0
# Creating the list
    numbers = [0] * 5
    greater_num = []

    n = int(input("Please enter a number: "))

    for index in range(5):
        numbers[index] = random.randint(0,20)
        index += 1

    numbers.sort()

    for index2 in range(5):
        if n < numbers[index2]:
            greater_num.append(numbers[index2])
            index2 += 1
            
    print(greater_num)
        
    
main()

# >>> 
# ==== RESTART: C:\Users\chris\Desktop\Python 3.7\Lab Assignment #15 EC.py ====
# Please enter a number: 12
# [14, 16]
# >>> 
# ==== RESTART: C:\Users\chris\Desktop\Python 3.7\Lab Assignment #15 EC.py ====
# Please enter a number: 0
# [1, 2, 5, 6, 17]
# >>> 
# ==== RESTART: C:\Users\chris\Desktop\Python 3.7\Lab Assignment #15 EC.py ====
# Please enter a number: 8
# [10, 12]
# >>> 
# ==== RESTART: C:\Users\chris\Desktop\Python 3.7\Lab Assignment #15 EC.py ====
# Please enter a number: 19
# [20]
# >>> 
# ==== RESTART: C:\Users\chris\Desktop\Python 3.7\Lab Assignment #15 EC.py ====
# Please enter a number: 20
# []
# >>> 
