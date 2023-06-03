# Lab Assignment #5 part 2
# Due 3/2/20

#                               Pseudocode
# Create tuple that stores the 4 card suits
# Create second tuple that stores the ranks/numbers of the cards
# Create full deck of cards in a list
# Implement a hand of 3 cards to the user in form of list
# Delete cards dealt from deck list to avoid same card appearing twice
# Do a second list of the computer and give them 3 cards as well
# Display all their cards for both of them


import random

# Lists for user hand, computer hand, and the card deck
user_hand = []
computer_hand = []
deck = []

# Tuples
suits = ('Diamond', 'Heart', 'Spade', 'Club')
nums = ('A', '2','3','4','5','6','7','8','9','10','J','Q','K')

# Creates the deck of 52 cards in a list
x = 0
y = 0
for y in range(4):
    for x in range(13):
        card = nums[x] + suits[y]
        add_card = deck.append(card)
        x += 1
    y += 1
  

# Deals user a random hand of 3 cards from the deck
for x in range(3):
    user_card = random.choice(deck)
    user_hand.append(user_card)
# Removes the dealt cards to avoid repeats
    deck.remove(user_card)
print('Your hand is:', user_hand)

# Deals the computer a random hand of 3 cards from the remaining deck
for x in range(3):
    computer_card = random.choice(deck)
    computer_hand.append(computer_card)
    deck.remove(computer_card)
print("The computer's hand is:", computer_hand)




