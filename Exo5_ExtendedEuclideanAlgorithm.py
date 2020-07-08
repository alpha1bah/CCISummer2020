# This program compute the gcd of two numbers using
# the Extended Euclidean Algorithm

def gcd(a, b):
    if b==0:
        return a
    return gcd(b, a%b)

n1 = eval(input("Enter the first number: "))
n2 = eval(input("Enter the second number: "))

print("gcd(", n1, ",", n2, ")=", gcd(n1, n2))