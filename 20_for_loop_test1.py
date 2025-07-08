number = int(input("Enter Number: "))
factorial = 1
for x in range(1,number + 1): # number + 1 because range exclude last values
    factorial = factorial * x
print("factorial:", factorial)