# This program is designed to solve Pell's equation
# for n ranging from 2 to 70 and x ranging from 1 to 70,000

"""
Pells' equation is : x^2 - ny^2 = 1
when we solve for y:  y = sqrt(1/n(x^2 - 1))
"""
import math
# Loop for generating N
n = 2
while n <= 3:
    # Loop for x
    x = 1
    while x <= 70:
        y = math.sqrt((x ** 2 - 1) / n)
        #if isinstance(y, int):
            #y = math.sqrt(1/n(x**2 - 1))
        print("(x,y)=  (",x , ",", y, ")  ", "for n equal to ", n)

        x += 1


    n += 1
