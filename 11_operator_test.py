#1)Atithmetic operator :-> +, -, *, /, %, **, //

#2)Assignment operator :-> =, +=, -=, *=, /= , %=, //=, **=, &=, |=, ^=, >>=, <<=

#3)Relational operator :-> <, >, <=, >= , == , !=

#4)Logical operator    :-> and , or , not

#5)Identity operator   :-> is , is not

#6)Membership operator :-> in, not in

#7)Bitwise Operator    :-> &, |, ^, ~, <<, >>

x = 3;
y = 4;

result = "sum is {0}"

z = x + y # Example of arithmetic operator
print(result.format(z))

x += y; # x = x + y Example of assignment operator
print(result.format(x))

bool = x > y # Example of relational operator
print(bool)

age = 21

bool = age > 18 and age < 40 # example of logical operator
print(bool)

x_fruit = ["apple", "banana"]
y_fruit = ["apple", "banana"]
z_fruit = x_fruit;

str = "address of {0} is {1}"
print(str.format("x_fruit", id(x_fruit)))
print(str.format("y_fruit", id(y_fruit)))
print(str.format("z_fruit", id(z_fruit)))

print(z_fruit is x_fruit)  # here o/p is True because x_fruit & z_fruit both poiting to same memory location, example of identity operator

print(x_fruit is y_fruit)  # here o/p is False because x_fruit & y_fruit both poiting to different memory location, example of identity operator

print("apple" in x_fruit) # check whether apple in x_fruit list return True if found else return false , example of membership operator

val = 12 & 13 # example of bitwise operator and 
print(val)

val = 12 | 13 # example of bitwise operator or 
print(val) 

val = 12 ^ 13 # example of bitwise operator XOR 
print(val)

val = 10 << 2 # example of bitwise operator left shift 1010 shifted to left i.e 101000 o/p is 40
print(val)

val = 10 >> 2 # example of bitwise operator right shift 1010 shifted to right i.e 0010 o/p is 2
print(val)