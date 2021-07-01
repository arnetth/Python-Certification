################################################################################
# Author: Hannah Arnett
# Date: 02/20/2021
# This program calculates the number of days in February in a given year.
################################################################################
year = int(input('Please input a year: ')) ## user inputs a year
if (year % 100 == 0 and year % 400 == 0): ## nested if statements calculate the number of days
    days = 29
elif (year % 100 != 0 and year % 4 == 0):
    days = 29
else:
    days = 28

print(f'In the year {year}, there are {days} days in February.') ## results
