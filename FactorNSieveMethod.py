# This program factor an integer n giving by the user

#Prompt the user to enter an integer less than or equal to 10,000
n = eval(input("Enter an integer less than or equal to 10,000: "))

myArray = []
print("The factors of ", n, " are: ")
for i in range(n+1):
    #b = -1
    myArray.append(-1)

for j in range(2, n+1):
    if myArray[j] == -1:
        for k in range(j, n+1, k=k+i):
            if myArray[k] == -1:
                myArray[k] = j

for i in range(1, n+1):
    print(myArray[i])
