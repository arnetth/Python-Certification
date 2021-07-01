################################################################################
# Author: Hannah Arnett
# Date: 03/08/2021
# This program outputs a list of prime numbers up to a user specified limit.
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
    primes = []
    num = int(input('Enter a positive integer (-1 to quit): '))
    if is_prime(num):
        primes.append()
        else:
            print(f'{num} is not a prime number.')

if __name__ == '__main__':
    main()
