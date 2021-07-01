################################################################################
# Author: Hannah Arnett
# Date: 3/15/2021
# Description: This program outputs 'hello turtle' using turtle graphics.
################################################################################

# Don't change this
from turtle import *

def draw_e():
    forward(60)
    left(90)
    circle(30, 320)

def draw_h():
    right(90)
    forward(150)
    left(180)
    forward(40)
    circle(-30, 180)
    forward(40)

def draw_l():
    forward(130)

def draw_o():
    circle(30, 360)

def draw_r():
    right(90)
    forward(60)
    left(180)
    forward(30)
    circle(-30, 90)

def draw_t():
    forward(130)
    left(180)
    forward(100)
    right(90)
    forward(30)
    left(180)
    forward(60)

def draw_u():
    right(90)
    forward(30)
    circle(30, 180)
    forward(30)
    right(180)
    forward(60)

def main():

    # Don't change this block --------------------------------------------------
    setup(600, 400)
    width(9)
    # --------------------------------------------------------------------------
    ## the following code prints hello turtle using functions for each letter
    ## hello
    penup()
    goto(-200, 170)
    pendown()
    draw_h()
    penup()
    goto(-100, 70)
    left(90)
    pendown()
    draw_e()
    penup()
    goto(0, 40)
    setheading(90)
    pendown()
    draw_l()
    penup()
    goto(60, 40)
    pendown()
    draw_l()
    penup()
    goto(180, 70)
    pendown()
    draw_o()
    ## turtle
    penup()
    goto(-200, -20)
    setheading(-90)
    pendown()
    draw_t()
    penup()
    goto(-150, -90)
    pendown()
    setheading(0)
    draw_u()
    penup()
    goto(-50, -90)
    setheading(0)
    pendown()
    draw_r()
    penup()
    goto(40, -20)
    setheading(-90)
    pendown()
    draw_t()
    penup()
    goto(120, -150)
    setheading(90)
    pendown()
    draw_l()
    penup()
    goto(170, -120)
    setheading(0)
    pendown()
    draw_e()

# Don't change this
if __name__ == '__main__':
    main()
    done()
