################################################################################
# Author: Hannah Arnett
# Date: 03/08/2021
# This program determines if an inputted number is a prime number.
################################################################################
def is_prime(num): # calculates if the input number is prime
    if (num > 1):
        for i in range(2, num): # if the number is divisible by more than itself and 1, it is not prime
            if num % i == 0:
                return False
            else: # if the number is only divisble by itself and 1, it is prime
                return True
    else: # if the number is not positive, 1, or 0, it is not prime
        return False

def main(): # accepts a positive integer and outputs the result of is_prime
    while(is_prime):
        num = int(input('Enter a positive integer (-1 to quit): '))
        if (num == -1): # quits function when -1 is entered
            break
        elif is_prime(num):
            print(f'{num} is a prime number.')
        else:
            print(f'{num} is not a prime number.')

if __name__ == '__main__':
    main()
