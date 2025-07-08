str = "Sum : <{0}>"
a = int(input("Enter first number: ")) # input() function always return user input in string format. here we are converting it in integer
b = int(input("Enter second number: ")) # input() function always return user input in string format. here we are converting it in integer
c = a + b
print(str.format(c))

name_start = input("Enter Name: ")[0] # it will read whole string from user and assign first character to name_start
print(name_start)

result = eval(input("Enter the expression: ")) # eval() function evaluate the expression from user input
print(result) 