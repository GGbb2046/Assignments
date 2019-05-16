"""
Author:         Tim Smith
Description:    A sample solution to Assignment02 challenge, using iteration (for loop) concepts (which will be covered
                in this class)
"""

import turtle

pen = turtle.Turtle()

for i in range(5) :

    pen.up()
    pen.setx(i*5)
    pen.sety(i*5)
    pen.down()

    # draw a T
    pen.left(90)    # point up
    pen.forward(100)
    pen.left(90)    # turn to the right
    pen.forward(50)
    pen.left(180)   # turn around
    pen.forward(100)

    # move to the next letter
    pen.up()
    pen.forward(150)

    # draw a C
    pen.left(180)
    pen.down()
    pen.forward(100)
    pen.left(90)
    pen.forward(100)
    pen.left(90)
    pen.forward(100)

    # move to the next letter
    pen.up()
    pen.forward(50)

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

    # back to the start, then move up and to the right by 5 pixels, and do it all again, 4 more times.


pen.hideturtle()



sandbox = turtle.Screen()
sandbox.mainloop()
