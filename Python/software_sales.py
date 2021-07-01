################################################################################
# Author: Hannah Arnett
# Date: 02/20/2021
# This program calculates percentage discounts of software purchases.
################################################################################
quantity = int(input('Please input the number of packages to be purchased: ')) ## user inputs number of packages
price = quantity * 99 ## calculates the price of the software quantity
if (quantity < 0): ## if else statements that print out the discount and price
    print('  Invalid Input!')
elif (quantity < 10):
    print(f'  No discount applied.\n  The final price for purchasing {quantity} packages is ${price:,.2f}.')
elif (quantity >= 10 and quantity <= 19):
    print(f'  10% discount applied.\n  The final price for purchasing {quantity} packages is ${(price*0.9):,.2f}.')
elif (quantity >= 20 and quantity <= 49):
    print(f'  25% discount applied.\n  The final price for purchasing {quantity} packages is ${(price*0.75):,.2f}.')
elif (quantity >= 50 and quantity <= 99):
    print(f'  35% discount applied.\n  The final price for purchasing {quantity} packages is ${(price*0.65):,.2f}.')
elif (quantity >= 100):
    print(f'  45% discount applied.\n  The final price for purchasing {quantity} packages is ${(price*0.55):,.2f}.')
