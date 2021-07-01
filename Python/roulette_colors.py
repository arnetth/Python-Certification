################################################################################
# Author: Hannah Arnett
# Date: 02/20/2021
# This program outputs the assigned color of an input number depending on if the number is even or odd and within a certain bracket.
################################################################################
pocket = int(input('Please enter a pocket number: ')) ## user inputs pocket number
if (pocket == 0): ## if else statements that assigns colors to numbers
    print(f'  Pocket {pocket} is green.')
elif (pocket >= 1 and pocket <= 10):
    if (pocket % 2 == 0):
        print(f'  Pocket {pocket} is black.')
    else:
        print(f'  Pocket {pocket} is red.')
elif (pocket >= 11 and pocket <= 18):
    if (pocket % 2 == 0):
        print(f'  Pocket {pocket} is red.')
    else:
        print(f'  Pocket {pocket} is black.')
elif (pocket >= 19 and pocket <= 28):
    if (pocket % 2 == 0):
        print(f'  Pocket {pocket} is black.')
    else:
        print(f'  Pocket {pocket} is red.')
elif (pocket >= 29 and pocket <= 36):
    if (pocket % 2 == 0):
        print(f'  Pocket {pocket} is red.')
    else:
        print(f'  Pocket {pocket} is black.')
elif (pocket < 0 or pocket > 36):
    print('  Invalid Input!')
