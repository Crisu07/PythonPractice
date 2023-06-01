# Lab Assignment #9
# 10/18/19

# 3 digit random number is range from 100 to 999
# demo program in lab

import random

def main():

    for x in range(1):

        number = message()
        
        number2 = message2()

    summation = number + number2
    
    user_input = int(input(' \t'))
    if user_input == summation:
        print("Congratulations, you have gotten the right answer")

    else:
        print("Stupid, the correct answer is", summation)

def message():
    number = random.randint(100,999)
    print('\t', number)
    return number

def message2():
    number2 = random.randint(100,999)
    print('+','\t',number2)
    return number2

main()

>>> 
====== RESTART: C:\Users\chris\Desktop\Python 3.7\Lab Assignment #9.py ======
	 898
+ 	 923
 	1821
Congratulations, you have gotten the right answer
>>> 
====== RESTART: C:\Users\chris\Desktop\Python 3.7\Lab Assignment #9.py ======
	 780
+ 	 116
 	21
Stupid, the correct answer is 896
>>> 
====== RESTART: C:\Users\chris\Desktop\Python 3.7\Lab Assignment #9.py ======
	 865
+ 	 921
 	1786
Congratulations, you have gotten the right answer
>>> 
