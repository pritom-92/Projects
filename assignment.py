print("Welcome to Daily Life Tracker Program")

name = input("Name:")
thour = int(input("Total hour:"))
db = float(input("Daily budget:"))


p = float(input("Studying Python:"))
c = float(input("Practicing coding:"))
oa = float(input("Other activities:"))

x = p+c+oa

print("Total activity hours planned for the day:", x)

# Expense Input

f = int(input("Food:"))
t = int(input("Transportation:"))
oe = int(input("Other expense:"))

y = f+t+oe

print("Total expense:", y)

if x > thour:
    print("You have planned more hours than available.")
else:
    print("Your daily plan is realistic.")

if y > db:
    print("You have exceeded your daily budget.")
else:
    print("You are within your daily budget.")

print("Hello,", name)
print("Total planned hours:", x)
print("Total expense", y)
print("Remaining budget", db-y)
