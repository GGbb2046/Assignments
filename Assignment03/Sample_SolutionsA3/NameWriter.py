"""
Author:         Tim Smith
Description:    A sample solution for Assignment02 (draw initials/monogram)
"""
import turtle

pen = turtle.Turtle()

pen.left(90)    # point up
pen.forward(100)
pen.left(90)    # turn to the right
pen.forward(50)
pen.left(180)   # turn around
pen.forward(100)
pen.up()
pen.forward(150)
pen.left(180)
pen.down()
pen.forward(100)
pen.left(90)
pen.forward(100)
pen.left(90)
pen.forward(100)
pen.up()
pen.forward(50)
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
pen.hideturtle()

sandbox = turtle.Screen()
sandbox.mainloop()
