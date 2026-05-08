print("Welcome to Smart Eligibility & Performance Checker")

name = str(input("Name:"))
age = int(input("Age:"))
score = float(input("Exam Score:"))
income = int(input("Monthly Income:"))
# age input
if age < 18:
    print("You are not eligible due to age restrictions.")
    age_eligible = False
else:
    print("Age requirement passed.")
    age_eligible = True

# score match
if score >= 90:
    grade = str("A")
    print("Grade: A")
elif score >= 75:
    grade = str("B")
    print("Grade: B")
elif score >= 60:
    grade = str("C")
    print("Grade: C")
else:
    print("Grade: Fail")

# eligibility
if (income < 20000 and score > 75) and age_eligible:  # only eligible >18
    x = str("Eligible")
    print("Eligible for scholarship support.")
else:
    x = str("Not eligible")
    print("Not eligible for scholarship.")

# deny <18
if age_eligible:
    if score >= 60:
        print("You passed the program.")
    else:
        print("You failed the program.")
else:
    print("Program access denied.")

# Final summary
print("Final Summary")

print("Name:", name)
print(age, "years")
print("Score obtained", score)
print("Grade:", grade)
if age_eligible:
    print("Scholarship:", x)
else:
    print("No scholarship")  # <18 scholarship will not be shown
