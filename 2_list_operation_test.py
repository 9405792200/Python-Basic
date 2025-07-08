number=[1,4,2,5,8,9,7,10,6,3]
print(number)
                
number[0] = 3;#list are mutale
print(number)

number.append(11); #it add element at last possition
print(number)

number.insert(4,6);  #it add element in the list at 4th index of the list 
print(number) 

number1=[1,2,3,4,5,6,3,6,7]
number1.remove(6)   #it will remove 6 from the list, only first occurence of 6 is removed from the list. If this element is not found in list then value error occured 
print("After 6 remove")
print(number1)

number.pop(3) #it will remove element which is at index 3rd. IF this index is not valid then index out of range index error occured
print(number); 

number.pop() # it will remove last element from the list
print(number) 

del number[2:4] #it will delete element from list starting from 2nd index to 4th index (exclusive)
print(number);

number.extend([12,13,14]) #it will add multiple value to number list
print(number)

numcopy = number.copy() # it will copy number list to numcopy
print(numcopy)

number.clear() #it will clear/empty number list
print(number)

number=[10,20,30,10,40,60,70,30,10];
print(number)
count = number.count(10) # it will return number of 10 in the list
print(count)

index = number.index(30); #it will return index of first occurence of element 30
print(index)

number.reverse() #it will reverse element of list is same list
print(number)


number.sort() # it will sort element of list in ascending order by default
print(number)

number.sort(reverse=True) # it will sort element of list in descending order
print(number)

number=[9,3,1,2,5,6,8,10,4,7]
print("Length of number :->")
print(len(number)) # it will return length of list number

print("Min element:->")
print(min(number))  # it will return min element from the list

print("Max element:->")
print(max(number))  # it will return max element from the list 

print("Sum element:->")
print(sum(number))  # it will return sum of element of the list

