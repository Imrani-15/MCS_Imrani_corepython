# how to build a countdown timer using the time Python module

import time



# define the countdown func.
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer,end=" \r") # end=" \r"
        time.sleep(1)
        t -= 1

    print("\nTime's up!! Stop the Game!")


# input time in seconds
t = input("Enter the time in seconds: ")

# function call
countdown(int(t))