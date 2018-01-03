"""
Uses turtle graphics to draw a four way button.
file: fourway_button.py
author: William Raffaelle
created: August 2016
"""

import turtle

turtle.title("4-Way Button")

def initialize():
    """
    Sets turtle in starting position with pen up.
    """
    turtle.up()
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)

def drawSquare():
    """
    Sets pen down and draws a square that encloses the buttons.
    """
    turtle.down()
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(200)

def drawCircle():
    """
    Sets pen up, positions turtle, and then sets pen down to draw the center circle.
    """
    turtle.up()
    turtle.left(90)
    turtle.forward(117)
    turtle.left(90)
    turtle.forward(100)
    turtle.down()
    turtle.circle(18)

def drawTriangle():
    """
    Sets pen down and is used to draw the four triangles (buttons).
    """
    turtle.down()
    turtle.forward(45)
    turtle.left(120)
    turtle.forward(45)
    turtle.left(120)
    turtle.forward(45)
    turtle.left(120)

def main():
    """
    Calls all the functions and positions turtle in a specific spot before each triangle is drawn.
    """
    initialize()
    drawSquare()
    drawCircle()

    turtle.up()
    turtle.left(90)
    turtle.forward(15)
    turtle.left(45)
    turtle.forward(110)
    turtle.left(150)
    drawTriangle()

    turtle.up()
    turtle.left(30)
    turtle.forward(110)
    turtle.right(90)
    turtle.forward(110)
    turtle.left(150)
    drawTriangle()

    turtle.up()
    turtle.left(30)
    turtle.forward(110)
    turtle.forward(110)
    turtle.left(150)
    drawTriangle()

    turtle.up()
    turtle.left(30)
    turtle.forward(110)
    turtle.left(90)
    turtle.forward(110)
    turtle.left(150)
    drawTriangle()

main()

turtle.done()