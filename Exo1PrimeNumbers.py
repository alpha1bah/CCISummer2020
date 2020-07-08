# This program aims to find prime numbers up to 10,000

n = 2
primeCounter = 0
while n <= 1_000:
    divisor = 0
    for j in range(2, n):
        if n % j == 0:
            divisor += 1


    if divisor == 0:
        primeCounter += 1
        print("Prime number ", primeCounter, "is : ", n)

    n += 1
