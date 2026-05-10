print("Welcome to Smart Student Life Management System")
name = str(input("Student name: "))
id = str(input("Student id: "))
dsh = int(input("Daily study hours:"))
mpm = int(input("Monthly pocket money: "))

str("menu") == True
while str("menu"):
    print("Main menu")
    print("1. Class Attendance Tracker")
    print("2. Study Session Manager")
    print("3. Exam Result Checker")
    print("4. Monthly Expense Tracker")
    print("5. Daily Problem Solver")
    print("6. Exit")
    option = int(input("Enter an option: "))
    if option == 1:
        total = int(input("Total classes: "))
        attended = int(input("Attended classes: "))
        percentage = (attended/total)*100
        if percentage >= 75:
            print("Eligible for exam")
        else:
            print("Not eligible for exam")
    elif option == 2:
        sub_name = str(input("Subject name: "))
        n = int(input("Number of study sessions: "))
        for i in range(1, n+1):
            print(f"Study session {i} completed")

        com = str(input("Did you complete all sessions? (yes/no): "))
        if com == str("yes"):
            print("Great consistency!")
        else:
            print("Try to improve tomorrow.")

    elif option == 3:
        python = float(input("Python: "))
        math = float(input("Mathematics: "))
        eng = float(input("English: "))
        total_marks = float(python+math+eng)
        average = float(total_marks/3)
        if average > 80:
            grade = str("A")
        elif average > 70:
            grade = str("B")
        elif average > 60:
            grade = str("C")
        else:
            grade = str("Fail")

        print(f"Final grade:{grade} ")

    elif option == 4:
        f_exp = int(input("Food expense: "))
        i_exp = int(input("Internet expense: "))
        t_exp = int(input("Transport expense: "))
        o_exp = int(input("Other expense: "))
        total_exp = f_exp+i_exp+t_exp+o_exp
        remain = mpm-total-total_exp
        if remain < 0:
            print("Budget Limit Crossed.")
        else:
            print("You managed your expenses well.")
    elif option == 5:
        print("1. Even or Odd Checker")
        print("2. Largest Number Finder")
        print("3. Simple Sum Calculator")
        op2 = int(input("Enter an option: "))

        if op2 == 1:
            n1 = int(input("Enter a number: "))
            if n1 % 2 == 0:
                print("Even")
            else:
                print("Odd")
        elif op2 == 2:
            a = int(input("A:"))
            b = int(input("B:"))
            c = int(input("C:"))

            if a > b:
                if a > c:
                    print("Largest is A")
                else:
                    print("Largest is C")
            else:
                if b > c:
                    print("Largest is B")
                else:
                    print("Largest is C")

        else:
            x = int(input("Num1: "))
            y = int(input("Num2: "))
            print(f"Sum is {x+y}")
    else:
        str("menu") == False
        break

countdown = int(input("Enter a countdown number: "))
for c in range(countdown, 0, -1):
    print(c)
    if c == 1:
        print("Session Finished Successfully.")

print("========== FINAL SUMMARY ==========")
print(f"Student name:{name}")
print(f"Stident id: {id}")
print(f"Attendance: {percentage}")
print(f"Last grade: {grade}")
print(f"Monthly Expense: {total_exp}")
print(f"Remaining Balance: {remain}")

print("Thank You For Using The System.")
