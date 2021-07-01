################################################################################
# Author: Hannah Arnett
# Date: 02/13/2021
# This program calculates the number of vines that can be planted in a row.
################################################################################
print('Enter the following quantities in feet.') # print statement
length = int(input('  How long is this row? '))
width = float(input('  How wide is the end-post assembly? '))
space = int(input('  How much space should be between the vines? '))
numgrape = (length-(2*width))/space
print(f'\nThis row has enough space for {int(numgrape)} vine(s).')
