from my_math import * # this is user created module 

num = float(input("Enter Number To Get Cube:"))
result = cube(num) # function call from my_math module
print("Cube:{0}".format(round(result,2)))

print("My Pi value:{0}".format(PI)) # To access variable PI from module my_math

print("fibonacci series:{0}".format(fibo(num)))

#Note: if you define function with same name in multiple module, 
#if that multiple module added then function call will be taken place from latest imported module  
