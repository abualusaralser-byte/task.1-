# Dictionary of months and their days 
months = {
    1:31, 2:28, 3:31, 4:30,
    5:31, 6:30, 7:31, 8:31,
    9:30, 10:31, 11:30, 12:31
    }
# Get month number from user 
month = int(input("Enter month number (1-12): "))
#Check if month exists in dictionary
if month in months:
# Special case for February
    if month == 2:
# Ask if it's a laep year 
        leap = input("Is it a leap year? (yes/no): ")
        if leap.lower() == "yes":
            print("29 days")
        else:
            print(months[month], "days")
    else:
# Print days for other months
        print(months[month], "days")
else:
# Invalid month number
       print("invalid month")
