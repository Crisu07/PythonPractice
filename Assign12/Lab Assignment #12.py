# Lab Assignment #12
# 10/25/19

import turtle

def main():

    turtle.showturtle()
    turtle.pendown()

    turtle.fillcolor('black')
    turtle.begin_fill()

    rectangle()
    
    turtle.end_fill()

    turtle.penup()
    turtle.goto(20,50)
    turtle.pendown()

    turtle.begin_fill()

    square()
    
    circle()

    turtle.end_fill()

# Function for drawing the rectangle    
def rectangle():
    for x in range(2):
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(50)
        turtle.left(90)

# Function for drawing the square in the middle
def square():
    for x in range(4):
        turtle.forward(60)
        turtle.left(90)

# Function for drawing the circle on top
def circle():
    turtle.penup()
    turtle.goto(50,110)
    turtle.pendown()
    turtle.circle(40)

main()
