################################################################################
# Author: Hannah Arnett
# Date: 3/13/2021
# Description: This program creates a spiral.
################################################################################

# Don't change this
from turtle import *

def main():

    # Don't change this block --------------------------------------------------
    setup(564, 564)
    width('5')
    # --------------------------------------------------------------------------

    # Write your code here
    #length = 0
    #forward(6)
    for i in range(39):
        #length += 6.0
        forward((i+1)*6)
        right(60)

# Don't change this
if __name__ == '__main__':
    main()
    done()
