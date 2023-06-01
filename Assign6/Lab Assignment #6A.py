# Lab-Assignment 6A
# 10/11/19

# 5 point extra cred, check to see he enters a negative number
# finish program first, only use what we learned
# make it start over if he enters a negative number
# or keep previous days of bugs and ignore the negative input

# Variables
bugs = 0
total_bugs = 0
days = 0

# Bugs collected each day
while days < 6:
    bugs = int(input("How many bugs did you collect today?: "))

# If user inputs a negative number of bugs, it will be ignored
    if bugs >= 0:
        total_bugs = total_bugs + bugs
        days += 1

print("The total number of bugs collected is: ", total_bugs)


>>> 
====== RESTART: C:\Users\chris\Desktop\Python 3.7\Lab Assignment #6A.py ======
How many bugs did you collect today?: 1
How many bugs did you collect today?: 2
How many bugs did you collect today?: 3
How many bugs did you collect today?: 4
How many bugs did you collect today?: 5
How many bugs did you collect today?: 6
The total number of bugs collected is:  21
>>> 
====== RESTART: C:\Users\chris\Desktop\Python 3.7\Lab Assignment #6A.py ======
How many bugs did you collect today?: 1
How many bugs did you collect today?: 2
How many bugs did you collect today?: 3
How many bugs did you collect today?: 4
How many bugs did you collect today?: -5
How many bugs did you collect today?: 6
How many bugs did you collect today?: 7
The total number of bugs collected is:  23
>>> 
====== RESTART: C:\Users\chris\Desktop\Python 3.7\Lab Assignment #6A.py ======
How many bugs did you collect today?: 1
How many bugs did you collect today?: 2
How many bugs did you collect today?: 3
How many bugs did you collect today?: -4
How many bugs did you collect today?: -5
How many bugs did you collect today?: 6
How many bugs did you collect today?: 7
How many bugs did you collect today?: 8
The total number of bugs collected is:  27
>>> 
