################################################################################
# Author: Hannah Arnett
# Date: 02/21/2021
# This program calculates the Reynolds number based on user input values of velocity, diameter, and temperature.
################################################################################
velocity = float(input('Enter the velocity of water in the pipe: ')) ## user inputs velocity
diameter = float(input('Enter the pipe\'s diameter: ')) ## user inputs diameter
temp = int(input('Enter the temperature in \u00B0C as 5, 10, or 15: ')) ## user inputs temperature, either 5, 10, or 15
if (temp == 5):
    rey = (velocity * diameter)/(1.49*10**-6)
elif (temp == 10):
    rey = (velocity * diameter)/(1.31*10**-6)
elif (temp == 15):
    rey = (velocity * diameter)/(1.15*10**-6)
print(f'The Reynolds number for flow at {velocity} m/s in a {diameter} m diameter pipe at {temp:.1f}\u00B0C is {rey:.2e}.')
