from functools import *

numbers = [1,2,3,4,5,6,7,8,9,10]
print("Orignal Numbers : {0}".format(numbers))

evens = list(filter(lambda num: num % 2 == 0, numbers))#filter Return those items of sequence for which function is true.
                                                       #if function is none, returns the item that are true. 
                                                       #If sequence is tuple or string, return the same type , else return list 
print("Even Numbers : {0}".format(evens))

double = list(map(lambda num: num * num, numbers)) #map return list by applying operation of mentioned function to each element of sequence
print("Double Numbers : {0}".format(double))

total = reduce(lambda x, y : x + y, numbers) #apply a function of two arguments to the items of a sequence from left to right so as to reduce it to single value
                                             #reduce function belongs to functools modules
print("Total:{0}".format(total))

