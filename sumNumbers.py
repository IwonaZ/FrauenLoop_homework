myNumbers = []

for n in range(1,1000):
    if n % 3 == 0 or n % 5 == 0:
        myNumbers.append(n)

sumNumbers = sum(myNumbers)

print(sumNumbers)