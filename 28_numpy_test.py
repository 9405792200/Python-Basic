from numpy import *

values = array([1,2,3,4,5]) # it create integer array

values = values + 5 # it will 5 to each element of array
print(values)

shallowvaluesCopy = values.view(); # it will create copy of values array as valuesCopy array, 
                                   # this is shallow copy that is change in one array reflect in another array as well   


deepvaluesCopy = values.copy() # it will create copy of values array as valuesCopy array, 
                               # this is deep copy that is change in one array will not reflect in another array 
values[0] = 11;
print(values)
print(shallowvaluesCopy)
print(deepvaluesCopy)

print(id(values))
print(id(shallowvaluesCopy))
print(id(deepvaluesCopy))