# Lab Assignment #16
# 12/06/19

def main():

    vowels = ['a', 'e', 'i', 'o', 'u']
# Ask user to input a string
    user_input = input("Please enter something: ")
    
    tv = vowel(vowels, user_input)
    
    tc = cont(user_input)

# Subtract amount of vowels from total alphabetic characters to get constanents
    print("Your string contained", tv, "vowels and", tc-tv, "constanents.")
    print("The number of characters used was", len(user_input))

def vowel(x,y):
# Converting string to lower case then calculating amount of variables in it
    total_v = 0
    Y = y.lower()
    for n in x:
        for z in Y:
            if n == z:
                total_v += 1
    return total_v

def cont(y):
# Counting the amount of alphabetic characters in the string
    total_con = 0
    for n in y:
        if n.isalpha():
            total_con += 1
    return total_con

main()

# >>> 
# ====== RESTART: C:\Users\chris\Desktop\Python 3.7\Lab Assignment #16.py ======
# Please enter something: hello
# Your string contained 2 vowels and 3 constanents.
# The number of characters used was 5
# >>> 
# ====== RESTART: C:\Users\chris\Desktop\Python 3.7\Lab Assignment #16.py ======
# Please enter something: How are you today?
# Your string contained 7 vowels and 7 constanents.
# The number of characters used was 18
# >>>
# ====== RESTART: C:\Users\chris\Desktop\Python 3.7\Lab Assignment #16.py ======
# Please enter something: Hello CECS 100 class
# Your string contained 4 vowels and 10 constanents.
# The number of characters used was 20
# >>> 
