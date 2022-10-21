# Write a Python program to convert month name to a number of days
month_name = input("Enter the month name :")
if month_name.title() == "february":
    print("No.of days: 28/29 days")
elif month_name.title() in ("april","june","september","november"):
    print("No of days: 30 days")
elif month_name.title() in ("January", "March", "May", "July", "August", "October", "December"):
    print("No.of days: 31 days")
else:
    print("Wrong month name")