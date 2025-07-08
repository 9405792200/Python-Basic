number = int(input("Enter Number: "))
index = 1
factorial = 1
while index <= number:
    factorial = factorial * index;
    index = index + 1
str = "factorial = <{0}>"
print(str.format(factorial))