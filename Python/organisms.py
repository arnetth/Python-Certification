################################################################################
# Author: Hannah Arnett
# Date: 03/01/2021
# This program predicts the approximate size of a population of organisms.
################################################################################

start = int(input('Starting number, in million: ')) ## user inputs starting number
avg = int(input('Average daily increase, in percent: ')) ## user inputs average daily increase in percentage
days = int(input('Number of days to multiply: ')) ## user inputs number of days to multiply
print('Day   Approx. Pop')
for i in range(days):
    if i == 0:
        pop = start
        print(f'  {i+1}        {pop:.4f}')
    elif i > 0 and i < 9:
        pop += pop * (avg/100)
        if pop > 10:
            print(f'  {i+1}       {pop:.4f}')
        else:
            print(f'  {i+1}        {pop:.4f}')
    else:
        pop += pop * (avg/100)
        print(f' {i+1}       {pop:.4f}')
