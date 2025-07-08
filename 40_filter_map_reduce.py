from functools import *

def is_even(num): # return true for even numbers
    return num % 2 == 0

numbers = [1,2,3,4,5,6,7,8,9,10]
print("Orignal List:{0}".format(numbers))

even = list(filter( is_even, numbers)) # filter Return those items of sequence for which function is true.
                                       # If function is none, returns the item that are true. 
                                       # If sequence is tuple or string, return the same type , else return list 
                                       # here is_even is function which return true for even numbers

print("Even Elements:{0}".format(even))

def squre(num): # return squre of numbers
    return num * num

squre = list(map(squre, numbers)) # map return list by applying operation of mentioned function to each element of sequence
                                  # here squre() is function which return num * num
print("Squre Elements:{0}".format(squre))

def sum(num1, num2):
    return num1 + num2;

total = reduce(sum , numbers) # apply a function of two arguments to the items of a sequence from left to right so as to reduce it to single value
                              # here sum() function of two arguments provide sum of numbers list
                              # reduce function belongs to functools modules                              
print("Total:{0}".format(total))



