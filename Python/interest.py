################################################################################
# Author: Hannah Arnett
# Date: 02/14/2021
# This program calculates interest in a given bank account over a period of time.
################################################################################
print('Please enter the following quantities.') # print statement
deposit = int(input('  How much is the initial deposit? '))
rate = float(input('  What is the annual interest rate in percent? '))
rate /= 100
frequency = int(input('  How many times per year is the interest compounded? '))
years = float(input('  How many years will the account be left to earn interest? '))

value = deposit*(1+(rate/frequency))**(frequency * years)
print(f'\nAt the end of {years} years, the account will be worth ${value:,.2f}.')
