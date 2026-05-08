import random
n = random.randint(1, 50)


for chance in range(4, 0, -1):
    x = int(input("Enter a number:"))
    if x > n:
        print("High")
    elif x < n:
        print("Low")
    else:
        print("Congratulations!!!")
        break


print("The number is", n)
print("Score", chance)
