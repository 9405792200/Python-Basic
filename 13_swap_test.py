a = 6 ;
b = 7 ;

str = "{0} swap a = {1} b = {2}"

print(str.format("Before", a, b))

a ,b = b ,a # put the value of b and a on stack and then reverse it this is called ROT_TWO() that is swap the two top most stack items 

print(str.format("After", a, b))