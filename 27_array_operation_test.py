from array import *

values = array('i', [10,20,30,40,50,10,90]) # unsigned integer array

print(values.typecode) # return datatype of array
print(values.buffer_info()) # return tuple of size two, inside tuple first element is address of an array and second element size of array 

values.append(100) # append() method add element at last of the array
print(values)

values.extend([-10,-20,-30]) # extend() method adds element to the array at last
print(values)

values.insert(1, -20) # insert(index, element) method add element to array at mentioned index which is parameter first
print(values)

val = values.pop() # pop() method remove last element from the array
print(val) 

val = values.pop(3) # pop(index) method remove element at mentioned index from array, if index is not valid then index out of range error occures  
print(val)

val = values.remove(10) # remove(element) method remove mentioned element from the array, if element not present in the list then ValueError occures 
print(values)

total = values.count(-20) # count(element) return count of element in the array
print(total)

possition = values.index(20) # index(element) return index of mentioned element from the array
print(possition)

values.reverse() # reverse() method reverse the list
print(values)

arraytolist = values.tolist(); # tolist() method convert array into list
print(arraytolist)

marks = array('i',[68,58,69,70,63]) # unsigned integer array
print(min(marks)) # it will return min element from array
print(max(marks)) # it will return max element from array
print(sum(marks)) # it will return sum of element of array
print(len(marks)) # it return number of element of array
