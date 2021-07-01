################################################################################
# Author: Hannah Arnett
# Date: 3/14/2021
# Description: This code prints a star when user inputs a specific number of points.
################################################################################

# Don't change this
from turtle import *

def main():

    # Don't change this block --------------------------------------------------
    setup(564, 564)
    width(7)
    side_length = 60 # Also the radius of a circle enclosed by the star.
    penup()
    goto(0, -side_length) # Start at the bottom of the star.
    pendown()
    # --------------------------------------------------------------------------

    # Write your code here
    points = int(input('How many points should the star have? '))

    A = 360/points
    B = 2*A
    color('green')
    fillcolor('cyan')
    begin_fill()
    right((180-B)/2)
    for i in range(points):
        forward(side_length)
        left(180-A)
        forward(side_length)
        right(180-B)
    end_fill()


# Don't change this
if __name__ == '__main__':
    main()
    done()
