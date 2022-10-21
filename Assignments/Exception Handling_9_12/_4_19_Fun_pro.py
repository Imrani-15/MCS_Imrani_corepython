while True:
    try:
        x = int(input("Please enter a number: "))
        print("My number is::",x)
        break
    except ValueError:
         print("Oops!  That was no valid number.  Try again...")
