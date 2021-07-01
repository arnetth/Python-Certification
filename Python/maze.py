################################################################################
# Author: Hannah Arnett
# Date: 3/13/2021
# Description This program moves the turtle through a maze.
################################################################################

# Don't change this
from turtle import *

def main():

    # Don't change this block --------------------------------------------------
    setup(564, 564)
    bgpic('maze.png')
    shape('turtle')
    color('green')
    width('5')
    step = 12
    # --------------------------------------------------------------------------

    # This code moves the turtle around the maze.
    forward(10)
    right(90)
    forward(85)
    left(90)
    forward(50)
    right(90)
    forward(25)
    left(90)
    forward(25)
    right(90)
    forward(95)
    left(90)
    forward(47)
    right(90)
    forward(25)
    left(90)
    forward(70)
    left(90)
    forward(48)
    right(90)
    forward(23)
    left(90)
    forward(183)
    right(90)
    forward(20)

# Don't change this
if __name__ == '__main__':
    main()
    done()
