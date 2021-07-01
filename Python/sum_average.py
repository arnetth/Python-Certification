################################################################################
# Author: Hannah Arnett
# Date: 03/01/2021
# This program calculates the sum and average of user input non-negative numbers.
################################################################################

numbers = float(input('Enter a non-negative number (negative to quit): ')) ## user inputs number
sum = 0 ## creates the variables for sum and average
avg = 0
count = 0
if numbers < 0: ## if at the start the user inputs a negative number it will stop asking for input
    print('No input.')
while (numbers == 0 or numbers > 0): ## if at the start the user inputs a non-negative number it will continue to ask for input
    sum += numbers ## calculates sum
    count += 1 ## increases the number count by 1 each time the user inputs a non-negative number
    numbers = float(input('Enter a non-negative number (negative to quit): ')) ## user inputs number and loop repeats until negative input
    if numbers < 0: ## when negative input the loop quits and outputs the sum and avg
        avg = sum / count
        print(f'Sum = {sum:.2f}')
        print(f'Average = {avg:.2f}')
