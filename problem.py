print("Welcome to Daily Life Problem Solver Toolkit")
str("yes") == True
while str("yes"):
    print("Select an option")
    print("1.Calculate sum of two numbers")
    print("2.Check even or odd")
    print("3.Find maximum of three numbers")
    option = int(input("Choose an option:"))

    if option == 1:
        x = int(input("Num1:"))
        y = int(input("Num2:"))
        print(f"Sum is{x+y}")
        d = x+y
    elif option == 2:
        z = int(input("Enter a number:"))
        if z % 2 == 0:
            print("Even")
            d = str("Even")
        else:
            print("Odd")
            d = str("Odd")
    else:
        a = int(input("A:"))
        b = int(input("B:"))
        c = int(input("C:"))
        if a > b:
            if a > c:
                print("A")
                d = str("A")
            else:
                print("C")
                d = str("C")
        else:
            if b > c:
                print("B")
                d = str("B")
            else:
                print("C")
                d = str("C")
    run = str(input("Do ypu want to run the program again?(yes/no)"))
    print("Summary")
    print(f"The result is {d}")

    if run == str("no"):
        break
