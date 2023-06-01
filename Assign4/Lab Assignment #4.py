# Lab Assignment 4
# 09/27/19

pocket = int(input("Please enter a number between 0 and 36: "))

# The only number that should be GREEN is 0
if (pocket == 0):
    print("The color of the pocket is GREEN")

# For pockets 1 through 10
elif (pocket >= 1 and pocket <= 10):
    if (pocket % 2 == 0):
        print("The color of the pocket is BLACK")
    else:
        print("The color of the pocket is RED")

# For pockets 11 through 18
elif (pocket >= 11 and pocket <= 18):
    if (pocket % 2 == 0):
        print("The color of the pocket is RED")
    else:
        print("The color of the pocket is BLACK")

# For pockets 19 through 28
elif (pocket >= 19 and pocket <= 28):
    if (pocket % 2 == 0):
        print("The color of the pocket is BLACK")
    else:
        print("The color of the pocket is RED")

# For pockets 29 through 36
elif (pocket >= 29 and pocket <= 36):
    if (pocket % 2 == 0):
        print("The color of this pocket is RED")
    else:
        print("The color of this pocket is BLACK")

# If user inputs a number outside of the number range of 0 to 36
else:
    print("You have entered an invalid number outside the number range")
