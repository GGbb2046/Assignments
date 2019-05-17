"""
Author:         Tim Smith
Description:    Sample solution for Class03 Ex04 (create a monogram drawing function, and demonstrate its usage)
"""

import turtle


def T(x, y, heading):
    pen = turtle.Turtle()
    pen.up()
    pen.setx(x + 50)
    pen.sety(y)
    pen.setheading(heading)
    pen.pendown()
    pen.speed(0)

    # draw a T
    pen.left(90)  # point up
    pen.forward(100)
    pen.left(90)  # turn to the right
    pen.forward(50)
    pen.left(180)  # turn around
    pen.forward(100)
    pen.up()
    pen.hideturtle()

    return


def C(x, y, heading):
    pen = turtle.Turtle()
    pen.up()
    pen.setx(x)
    pen.sety(y)
    pen.setheading(heading)
    pen.pendown()
    pen.speed(0)

    # draw a C
    pen.forward(100)
    pen.left(90)
    pen.penup()
    pen.forward(100)
    pen.left(90)
    pen.pendown()
    pen.forward(100)
    pen.left(90)
    pen.forward(100)
    pen.up()
    pen.hideturtle()

    return


def S(x, y, heading):
    pen = turtle.Turtle()
    pen.up()
    pen.setx(x)
    pen.sety(y)
    pen.setheading(heading)
    pen.pendown()
    pen.speed(0)

    # draw an S
    pen.down()
    pen.forward(100)
    pen.left(90)
    pen.forward(50)
    pen.left(90)
    pen.forward(100)
    pen.right(90)
    pen.forward(50)
    pen.right(90)
    pen.forward(100)

    pen.up()
    pen.hideturtle()

    return


sandbox = turtle.Screen()

# draw word
T(-220, 0, 0)
C(-110, 0, 0)
S(0, 0, 0)
T(110, 0, 0)
S(220, 0, 0)

# draw word with letters spun 45 degrees
T(-220, 150, 45)
C(-110, 150, 45)
S(0, 150, 45)
T(110, 150, 45)
S(220, 150, 45)

sandbox.mainloop()
