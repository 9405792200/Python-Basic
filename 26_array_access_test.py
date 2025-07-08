from array import *

marks = array('i',[60,33,56,78,23,56])

print(marks)  # it print full array

print(marks[0])     #it will print element at zeorth index
print(marks[2:4])   #it will print element start from index 2 and end at index 4, second parameter is exlusive
print(marks[:4])    #it will print element start from index zeroth to 4th index,second parameter is exlusive
print(marks[4:])    #it will print element start from index 4th to end of array
print(marks[2:89])  #it will print element start from index 2nd to end of array

print(marks[-1])    #it will print element at index -1 
print(marks[-3:-1]) #it will print element start from index -3 to -1 here second parameter is exclusive
print(marks[:-2])   #it will print element from zeorth index to -2, here second parameter is exclusive
print(marks[-2:])   #it will print element from -2 index to end of array
print(marks[-2:-10]) #it will return empty array because indexing always move from left to right

for x in marks: # to access each element of the array
    print(x)
    
copyofmarks = array(marks.typecode,(x for x in marks)) # to copy one array to another, here typecode return datatype of array marks 
print(copyofmarks);
