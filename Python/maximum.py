################################################################################
# Author: Hannah Arnett
# Date: 03/07/2021
# This program compares two user inputted numbers and outputs the larger number.
################################################################################
def max_of_two(f, s): ## compares the two numbers
    if (f > s):
        print(f'{f} is greater.')
        return f
    elif (f < s):
        print(f'{s} is greater.')
        return s

def main(): ## main function calls on the falling_distance function
    first = int(input('Enter the first integer: '))
    second = int(input('Enter the second integer: '))
    max_of_two(first, second)

if __name__ == '__main__':
    main()
