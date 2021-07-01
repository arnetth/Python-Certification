################################################################################
# Author: Hannah Arnett
# Date: 03/01/2021
# This program calculates the average monthly rainfall of a given number of years based on user input.
################################################################################
years = int(input('Enter the number of years: ')) ## user inputs number of years
months = 0
total = 0 ## variables for total number of months, total amount of rainfall
if years == 0: ## if user inputs 0 years it will print invalid input
    print('Invalid input.')
if years > 0: ## if user inputs positive number of years the program will proceed
    months = 12 * years ## calculates the total number of months of number of years inputted
    for i in range(years): ## accesses the years
        print(f'  For year No. {i+1}') ## outputs each year
        for j in range(12): ## asks for input for each month of each year and calculates avg, total
            if j == 0:
                rain = float(input('    Enter the rainfall for Jan.: '))
                while rain < 0:
                    print('    Invalid input, please try again.')
                    rain = float(input('    Enter the rainfall for Jan.: '))
                total += rain
            elif j == 1:
                rain = float(input('    Enter the rainfall for Feb.: '))
                while rain < 0:
                    print('    Invalid input, please try again.')
                    rain = float(input('    Enter the rainfall for Feb.: '))
                total += rain
            elif j == 2:
                rain = float(input('    Enter the rainfall for Mar.: '))
                while rain < 0:
                    print('    Invalid input, please try again.')
                    rain = float(input('    Enter the rainfall for Mar.: '))
                total += rain
            elif j == 3:
                rain = float(input('    Enter the rainfall for Apr.: '))
                while rain < 0:
                    print('    Invalid input, please try again.')
                    rain = float(input('    Enter the rainfall for Apr.: '))
                total += rain
            elif j == 4:
                rain = float(input('    Enter the rainfall for May.: '))
                while rain < 0:
                    print('    Invalid input, please try again.')
                    rain = float(input('    Enter the rainfall for May.: '))
                total += rain
            elif j == 5:
                rain = float(input('    Enter the rainfall for Jun.: '))
                while rain < 0:
                    print('    Invalid input, please try again.')
                    rain = float(input('    Enter the rainfall for Jun.: '))
                total += rain
            elif j == 6:
                rain = float(input('    Enter the rainfall for Jul.: '))
                while rain < 0:
                    print('    Invalid input, please try again.')
                    rain = float(input('    Enter the rainfall for Jul.: '))
                total += rain
            elif j == 7:
                rain = float(input('    Enter the rainfall for Aug.: '))
                while rain < 0:
                    print('    Invalid input, please try again.')
                    rain = float(input('    Enter the rainfall for Aug.: '))
                total += rain
            elif j == 8:
                rain = float(input('    Enter the rainfall for Sep.: '))
                while rain < 0:
                    print('    Invalid input, please try again.')
                    rain = float(input('    Enter the rainfall for Sep.: '))
                total += rain
            elif j == 9:
                rain = float(input('    Enter the rainfall for Oct.: '))
                while rain < 0:
                    print('    Invalid input, please try again.')
                    rain = float(input('    Enter the rainfall for Oct.: '))
                total += rain
            elif j == 10:
                rain = float(input('    Enter the rainfall for Nov.: '))
                while rain < 0:
                    print('    Invalid input, please try again.')
                    rain = float(input('    Enter the rainfall for Nov.: '))
                total += rain
            elif j == 11:
                rain = float(input('    Enter the rainfall for Dec.: '))
                while rain < 0:
                    print('    Invalid input, please try again.')
                    rain = float(input('    Enter the rainfall for Dec.: '))
                total += rain
    avg = total / months
    print(f'There are {months} months.\nThe total rainfall is {total:.2f} inches.\nThe monthly average rainfall is {avg:.2f} inches.')
