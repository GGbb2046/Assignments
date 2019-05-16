"""
Author:         Tim Smith
Description:    A sample solution to Assignment02 challenge, using only concepts covered last class
"""
import turtle

pen = turtle.Turtle()

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

# second writing of the name
pen.up()
pen.setx(5)
pen.sety(5)
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


# third writing

pen.up()
pen.setx(10)
pen.sety(10)
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

# fourth writing

pen.up()
pen.setx(15)
pen.sety(15)
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
pen.up()

# fifth writing


pen.setx(20)
pen.sety(20)
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


pen.hideturtle()



sandbox = turtle.Screen()
sandbox.mainloop()
