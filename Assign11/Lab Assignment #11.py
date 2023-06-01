# Lab Assignment #11
# 10/25/19

import turtle

def main():

    turtle.showturtle()
    turtle.pendown()

    
# Forgot to make border red on lab and center the stop sign
#   turtle.pencolor("red")
    turtle.fillcolor("red")
    turtle.begin_fill()

# Drawing the octagon for the stop sign
    octagon()
    
    turtle.end_fill()
    
    turtle.penup()
    turtle.goto(-27,67)
    turtle.pendown()

# Printing the word STOP
# Change pen color back to black for STOP
    turtle.pencolor("black")
    turtle.write("STOP", font = ("Comic Sans", 40))
    turtle.hideturtle()

def octagon():
    for x in range(8):
        turtle.forward(80)
        turtle.left(45)

main()
