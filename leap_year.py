x = int(input("Year:"))

if (x % 4 == 0 and x % 100 != 0) or x % 400 == 0:
    print("leap year")
else:
    print("not leap year")
