number=(1,4,2,5,8,9,7,10,6,3)
print(number)
                
#number[0] = 3; # this is error because tuple are immutale ie we can not assign value to it

#number.append(11); #tuple dont have this method because tuple are immutale

#number.insert(4,6);  #tuple dont have this method because tuple are immutale

number1=(1,2,3,4,5,6,3,6,7)
#number1.remove(6)   #tuple dont have this method because tuple are immutale

#number.pop(3) #tuple dont have this method because tuple are immutale  

#number.pop() # tuple dont have this method because tuple are immutale

#del number[2:4] #Item deletion not support by tuple bacause tuple are immutale


#number.extend([12,13,14]) #tuple dont have this method because tuple are immutale


#numcopy = number.copy() # tuple dont have this method because tuple are immutale


#number.clear() # tuple dont have this method because tuple are immutale

number=(10,20,30,10,40,60,70,30,10);
print(number)
count = number.count(10) # it will return number of 10 in the tuple
print(count)

index = number.index(30); #it will return index of first occurence of element 30
print(index)

#number.reverse() #tuple dont have this method


#number.sort() # #tuple dont have this method

#number.sort(reverse=True) # #tuple dont have this method

number=(9,3,1,2,5,6,8,10,4,7)
print("Length of number :->")
print(len(number)) # it will return length of tuple number

print("Min element:->")
print(min(number))  # it will return min element from the tuple

print("Max element:->")
print(max(number))  # it will return max element from the tuple 

print("Sum element:->")
print(sum(number))  # it will return sum of element of the tuple

