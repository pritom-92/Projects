l = int(input("Enter a number: "))
count = 0
loop = 0
for x in range(2, l):
    n = x
    is_prime = True
    for i in range(2, n):
        loop += 1
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        count += 1
        print(f"{count}-{n} is prime")

print(loop)
