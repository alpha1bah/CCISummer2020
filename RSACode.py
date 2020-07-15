# This program decodes a message using RSA

# Define a function to find the gcd of phi and e
def gcd(a, b):
    if b==0:
        return a
    return gcd(b, a%b)

# Prompts the user to choose two very large primes
p = eval(input("Enter the first prime number: "))
q = eval(input("Enter the second prime number: "))

# Compute the modulo n
n = p * q

# Compute phi
phi = (p-1) * (q-1)
# Prompte the user to chose e
e = eval(input("Enter the value of \"e\" such as e is greater than 2 and co-prime with phi: "))
gcd(phi, e)
print("the gcd of phi=", phi, " and e=", e, " is: ", gcd(phi, e))
while(e<=2 or gcd(phi, e) != 1):
    e = eval(input("You entered a wrong value for e, re-enter the value of e again: "))

# Implement here the algorithm of finding d

"""
e1 = e
d1 = 1
while e1 != 1:
    phi1 = phi
    q1 = phi // e
    e1 *= q1
    d1  *= q1

    e1
    if e1>0:
        phi1, e1 = e1, phi1 - q1 * e1

"""

"""
phi, e = 40, 7
"""
a11 = a12 = phi
a21, a22 = e, 1
#print("phi=", phi, "e=", e, "\na11=", a11, "a12=", a12, "\na21=", a21, "a22=", a22)
print("phi=", phi, "e=", e, "\n", "\n")
print(a11, "\t", a12)
print(a21, "\t", a22)

while a21 != 1:
    q1 = a11 // a21
    dif1 = a11 - q1 * a21
    a11 = a21
    if dif1 > 0:
        a21 = dif1
    else: a21 = dif1 % phi

    dif2 = a12 - q1 * a22
    a12 = a22
    if dif2 > 0:
        a22 = dif2
    else: a22 = dif2 % phi


print("d=", a22)
d=a22

# Prompt the user to enter the value he wants to send
message = input("Enter a character for your message here:")
ASCCI_of_original_message = ord(message)

print("Original message before encryption:", message, " and it's ASCII is:", ASCCI_of_original_message)

#Encryption
encrypted = ASCCI_of_original_message**e % n
print("The encrypted message is: ", chr(encrypted), " and it's ASCII is: ", encrypted)

# Decryption
originam_m = encrypted**d % n
print("The original message after decryption is: ",chr(originam_m), " and it's ASCII is ",originam_m)




