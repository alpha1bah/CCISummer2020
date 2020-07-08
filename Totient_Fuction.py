# This program is design to compute the Euler Totient Function
# of a giving number n

# Function for gcd of a and b
def gcd(a, b):
    if a == 0 :
        return b

    return gcd(b%a, a)

# The Totient Function
def phi(n):
    phi_counter = 1
    for i in range(2, n):
        if gcd(i, n) == 1:
            phi_counter += 1
    return phi_counter

number = eval(input("Enter the number you want to find the phi:"))
for n in range(1, number):
    print("phi(", n, ")=", phi(n))