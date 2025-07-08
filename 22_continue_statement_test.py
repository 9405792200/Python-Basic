number = int(input("Enter Number: "))
index = factorial = 1
while index <= number:
    if index == 1:
        index = index + 1 #need to increment here otherwise it will be in infinite loop due to above condition
        continue #below block will not execute and continue for next iteration
    factorial = factorial * index
    index = index + 1
    
print("Factorial = ", factorial)