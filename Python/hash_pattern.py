################################################################################
# Author: Hannah Arnett
# Date: 02/20/2021
# This program outputs the assigned color of an input number depending on if the number is even or odd and within a certain bracket.
################################################################################
lines = int(input('Enter the number of lines: ')) ## user inputs number of lines they want
## print("##") ## this will start off the lines with no spaces
for i in range(lines): ## creates the rows
    for j in range(i+1): ## creates the columns of # and spaces
        space = j * " " ## defines the number of spaces needed in each line
    print("#" + space, end="#") ## prints the results
    print('') # start a new line
