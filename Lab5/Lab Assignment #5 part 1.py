# Chris Nguyen
# 025513031
# CECS 174 Section 05
# Lab Assignment #5 Part 1
# Due 3/2/20

#                               Pseudocode
# Create tuple that consists of the right answers for the quiz
# Ask user for input on the student's test scores with spaces in between
# Put user input into a list
# Capitalize the list in order to compare with corect answers
# Go through each element and compare answers
# Tally how many correct answers there were
# Convert score to percentage
# Display Results
# Ask if user wants to grade another student
# Repeat if yes, end if not

# Tuple containing the right answers
correct_ans = ('C','B','A','A','D','C','C','B','D','D','A','C','D','A','B','B')

# Loop to continue grading if needed
reply = 'Y'
while reply == 'Y':
    counter = 0
    user_answers = list(input('Enter answers separated by spaces:').split())
    for x in range(len(user_answers)):
        if correct_ans[x] == user_answers[x].upper():
            counter += 1

# If user got 15 or more answers correct, they get a 100%
    if counter >= 15:
        test_score = 100
    else:
        test_score = (counter*100) / 15
        test_score = format(test_score, '.2f')

# Display results
    print('You have inputed:', user_answers)
    print('The student has', counter, 'answers correct',\
          'and the percent score is', test_score, '%')

# Asks user if they want to repeat
    user_input = input('Continue grading for more students? (Y/N or y/n):')
    user_input = user_input[0].upper()
    reply = user_input
