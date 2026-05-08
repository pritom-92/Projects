print("Enter current date-->")
date1 = int(input("Enter date:"))
month1 = int(input("Enter month:"))
year1 = int(input("Enter year:"))
print("Today's date:", date1, "/", month1, "/", year1)

print("Give date of birth")
date = int(input("Enter date:"))
month = int(input("Enter month:"))
year = int(input("Enter year:"))
print("Date of birth is", date, "/", month, "/", year)
if year > year1:
    print("Invalid")
else:
    if month < month1:
        x = year1-year
        print("Age is:", year1-year)
    elif (month == month1 and date <= date1):
        x = year1-year
        print("Age is:", year1-year)
    elif month > month1 or (month == month1 and date > date1):
        x = year1-year-1
        print("Age is:", year1-year-1)

if x >= 18:
    print("Eligible for NID")
else:
    print("Not Eligible for NID")
