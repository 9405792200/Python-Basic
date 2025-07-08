def factorial(num):
    result = 1
    for x in range(1, num + 1):
        result = result * x
    return result
    
    
num = int(input("Enter the number :"))
fact = factorial(num)

print("Factorial :",fact)