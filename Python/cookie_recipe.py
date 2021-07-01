################################################################################
# Author: Hannah Arnett
# Date: 02/15/2021
# This program calculates the amount of ingredients, in cups, to make a specific amount of cookies.
################################################################################
cookies = int(input('How many cookies do you want to make? '))
print(f'To make {cookies} cookies, you will need:')
sugar = (1.5/48)*cookies
butter = (1/48)*cookies
flour = (2.75/48)*cookies
print(f'{sugar:7.2f} cups of sugar\n{butter:7.2f} cups of butter\n{flour:7.2f} cups of flour')
