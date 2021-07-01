################################################################################
# Author: Hannah Arnett
# Date: 02/20/2021
# This program takes the input of time in seconds, then converts the time to hours, minutes, and seconds depending on how many seconds were inputted.
################################################################################
time = int(input('Please enter a time in seconds. ')) ## user inputs time in seconds
## if else statements that converts the seconds into hours, minutes, and seconds depending on how many seconds were inputted
if (time < 60): ## calculations for less than 60 seconds
    print('  The number of seconds is less than one minute.')
elif (time >= 60 and time < 3600): ## calculations for minutes below one hour
    minutes = time // 60
    seconds = time % 60
    if (seconds == 0): ## if seconds is 0, it will not be included in the print statement
        print(f'  {time} seconds is: {minutes} minute(s).')
    else:
        print(f'  {time} seconds is: {minutes} minute(s) and {seconds} second(s).')
elif (time >= 3600 and time < 86400): ## calculations for hours below one day
    hours = time // 3600
    minutes = (time % 3600) // 60
    seconds = (time % 3600) % 60
    if (minutes == 0): ## if minutes is 0, it will not be included in the print statement
        print(f'  {time:,.0f} seconds is: {hours} hour(s) and {seconds} second(s).')
    elif (seconds == 0): ## if seconds is 0, it will not be included in the print statement
        print(f'  {time:,.0f} seconds is: {hours} hour(s) and {minutes} minute(s).')
    elif (seconds == 0 and minutes == 0): # if seconds and minutes are 0, they will not be included in the print statement
        print(f'  {time:,.0f} seconds is: {hours} hour(s).')
    else:
        print(f'  {time:,.0f} seconds is: {hours} hour(s), {minutes} minute(s) and {seconds} second(s).')
elif (time >= 86400): ## calculations for days
    days = time // 86400
    hours = (time % 86400) // 3600
    minutes = ((time % 86400) % 3600) // 60
    seconds = ((time % 86400) % 3600) % 60
    if (days >= 1 and minutes == 0 and seconds == 0 and hours == 0):
        print(f'  {time:,.0f} seconds is: {days} day(s).')
    elif (days >= 1 and hours == 0 and seconds == 0 and minutes != 0):
        print(f'  {time:,.0f} seconds is: {days} day(s) and {minutes} minute(s).')
    elif (days >= 1 and minutes == 0 and seconds == 0 and hours != 0):
        print(f'  {time:,.0f} seconds is: {days} day(s) and {hours} hour(s).')
    elif (days >= 1 and minutes == 0 and seconds != 0 and hours != 0):
        print(f'  {time:,.0f} seconds is: {days} day(s), {hours} hour(s) and {seconds} second(s).')
    elif (days >= 1 and minutes != 0 and seconds == 0 and hours != 0):
            print(f'  {time:,.0f} seconds is: {days} day(s), {hours} hour(s) and {minutes} minute(s).')
    elif (days >= 1 and minutes == 0 and seconds != 0 and hours == 0):
            print(f'  {time:,.0f} seconds is: {days} day(s) and {seconds} second(s).')
    elif (days >= 1 and minutes != 0 and seconds != 0 and hours == 0):
            print(f'  {time:,.0f} seconds is: {days} day(s), {minutes} minute(s) and {seconds} second(s).')
    elif (days != 0 and hours != 0 and minutes !=0 and seconds != 0):
        print(f'  {time:,.0f} seconds is: {days} day(s), {hours} hour(s), {minutes} minute(s) and {seconds} second(s).')
