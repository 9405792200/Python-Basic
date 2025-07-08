decimal_num = 35
str = "{0} of {1} = {2}"

binary = bin(decimal_num); # return binary of input number , input number can be of different format decimal, octal(0o), hexa decimal(0x)
octal =  oct(decimal_num); # return octal of input number, input number can be of different format decimal, binary(0b), hexa decimal(0x)
hexa =   hex(decimal_num); # return hexa of input number, input number can be of different format decimal, octal(0o), binary(0b)

print(str.format("binary", decimal_num, binary))
print(str.format("octal", decimal_num, octal))
print(str.format("hexa", decimal_num, hexa))

decimal = 0b10011 # this number represent binary number, assigment operator assign decimal number 
print(decimal)

decimal = 0o37 #this number represent octal number, assigment operator assign decimal number
print(decimal)

decimal = 0x56 # this number represent hexadecimal number, assigment operator assign decimal number
print(decimal)

