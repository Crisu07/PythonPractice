# Lab-Assignment 6B
# 10/11/19

# must show how we did the math on the input
# 3% a year not a semester
# MUST calculate all the numbers in your code

increase_a_year = 0.03
starting = 8000.00

tuition = starting

print("Year\t Project Tuition(per Semester)")

for year in range(5):
    tuition += (tuition * increase_a_year)
    print((year+1), '\t', '$', format(tuition,'.2f'))
    print((year+1), '\t', '$', format(tuition,'.2f'))

>>> 
 RESTART: C:/Users/chris/Desktop/Python 3.7/Lab Assignment #6B (correct one).py 
Year	 Project Tuition(per Semester)
1 	 $ 8240.00
1 	 $ 8240.00
2 	 $ 8487.20
2 	 $ 8487.20
3 	 $ 8741.82
3 	 $ 8741.82
4 	 $ 9004.07
4 	 $ 9004.07
5 	 $ 9274.19
5 	 $ 9274.19
>>> 
