################################################################################
# Author: Hannah Arnett
# Date: 03/07/2021
# This program calculates the distance that an object will fall in a given length of time.
################################################################################
g = 9.81 ##  gravitational force
print('Time (s)  Distance (m)\n----------------------')
def main(): ## main function calls on the falling_distance function
    for i in range(10):
        time = i+1
        d = falling_distance(time)
        print(f'{(i+1):8d}{d:14.2f}')

def falling_distance(t): ## calculates the distance using the provided equation
    d = (1/2)*g*t**2
    return d

main()
