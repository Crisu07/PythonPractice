# Lab Assignment 17
# 12/6/19

def main():

# Ask user for input
    user_input = input("Please enter a string: ")
    cap_input = capitalize(user_input)
    print(cap_input)

def capitalize(x):
    string1 = ''
    string2 = ''
    
# Break up each word in the string
    words = x.split()

# Check to see if it is a new sentence
    for n in words:
        if n[-1] == '!' or n[-1] == '.' or n[-1] == '?':
            n = string1 + n    
# Creating new word that capitalizes first letter of every sentence
            new_word = n[0].upper() + n[1:]
            
            new_word = new_word + ' '
# Adding new word to the string
            string2 += new_word
            string1 = ''
            
        else:
            string1 += n
            string1 += ' '
            
    return string2


main()

# >>> 
# ====== RESTART: C:\Users\chris\Desktop\Python 3.7\Lab Assignment #17.py ======
# Please enter a string: hello. my name is Joe. what is your name?
# Hello. My name is Joe. What is your name? 
# >>> 
# ====== RESTART: C:\Users\chris\Desktop\Python 3.7\Lab Assignment #17.py ======
# Please enter a string: whoa! what are you doing? hello there. wow!
# Whoa! What are you doing? Hello there. Wow! 
# >>> 
# ====== RESTART: C:\Users\chris\Desktop\Python 3.7\Lab Assignment #17.py ======
# Please enter a string: hey! the program was hard. really?
# Hey! The program was hard. Really? 
# >>> 
