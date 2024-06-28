'''
        THIS IS A SIMPLE PYTHON COUNTDOWN PROGRAM IN PYTHON
        => It makes use of the time module and a function basically called the sleep() function,
        => The sleep function renders the console screen inactive for a certain amount of time.
        => Also it makes use of for loops and depends on user input
        => Also we will import the os module to be able to clear the screen after displaying a particular time
           for a second.


'''

import time
import os

GREEN = "\033[32m" # This are unicode for coloring the console screen
RED = "\033[31m"

yourTime = int(input("Enter the time in second: "))
for x in reversed(range(yourTime)):
    seconds = x % 60 # Seconds can only move from 1 to 59, reason for % 60
    minutes = int(x / 60) % 60 # minutes can also move only from 1 to 59 reason for the %60 after the /60
    hours = int(x/3600) # Here noo need for modulus since we have 3600 seconds in one hour.
    if hours == 0 and minutes == 0 and seconds <=20:
        print(f"{RED} {hours:02}:{minutes:02}:{seconds:02}")
        time.sleep(1)
        os.system("cls")
    else:
        print(f"{GREEN} {hours:02}:{minutes:02}:{seconds:02}")
        time.sleep(1)
        os.system("cls")

print("TIME'S UP BRO!")
    



