number={1,4,2,5,8,9,7,10,6,3}
print(number)
                
#number[0] = 3; #set dont support indexing hence item assignment not supported for set

#number.append(11); #set dont have this method

number.add(12); #it will add element to set If the element already exists, the add() method does not add the element
print(number);

#number.insert(4,6);  #set dont have this method because set dont support for indexing 

number1={1,2,3,4,5,6,3,6,7}
number1.remove(6)   #it will remove element 6 from the set,  If this element is not found in set then key error occured 
print("After 6 remove")
print(number1)

number1.discard(9)  # it will remove element 9 from the set, If this element is not found in set then it dont throw any error
print("After 9 remove")
print(number1)

#number.pop(3) #set dont have this method because set dont support for indexing

x = number.pop() # this method remove random element from the set
print(x) 

#del number[2:4] #in set deletion not supported because of unindexing
#print(number);

#number.extend([12,13,14]) #set dont have extend method
#print(number)

number.update([10,20,40]) #this method add element in number set If an item is present in both sets, only one appearance of this item will be present in the number set
print(number)

numcopy = number.copy() # it will copy number set to numcopy
print(numcopy)

number.clear() #it will clear/empty number set
print(number)

number={10,20,30,10,40,60,70,30,10};
print(number)
#count = number.count(10) # set dont have this method because in set only unique element are supported

#index = number.index(30); #set dont have this method because set dont support for indexing
#print(index)

#number.reverse() #set dont have this method
#print(number)


#number.sort() #set dont have this method
#print(number)

#number.sort(reverse=True) #set dont have this method
#print(number)

ndrteam = {"Bhushan","Priyati","Prema","Swapnil","Hena","Amey"}
fullteam = {"Bhushan","Priyati","Prema","Swapnil","Hena","Amey","Mayur","Swaraj","Apurva","Vaibhav"}
print("ndrteam")
print(ndrteam)

print("fullteam")
print(fullteam)


diff = fullteam.difference(ndrteam) #The returned set contains items that exist only in the first set, and not in both sets i.e it does diff = fullteam - ndrteam difference() method returns a new set, without the unwanted items
print("fullteam - ndrteam")
print(diff); 

diff = ndrteam.difference(fullteam) #The returned set contains items that exist only in the first set, and not in both sets i.e it does diff = ndrteam - fullteam difference() method returns a new set, without the unwanted items
print("ndrteam - fullteam")
print(diff); 

fullteam.difference_update(ndrteam) #it does fullteam = fullteam - ndrteam the difference_update() method removes the unwanted items from the original set
print("fullteam = fullteam - ndrteam")
print(fullteam);

fullteam = {"Bhushan","Priyati","Prema","Swapnil","Hena","Amey","Mayur","Swaraj","Apurva","Vaibhav"} #Again assign it because fullteam got change in above statement
ndrteam.difference_update(fullteam)
print("ndrteam = ndrteam - fullteam") #it does ndrteam = ndrteam - fullteam the difference_update() method removes the unwanted items from the original set
print(ndrteam)

ndrteam = {"Bhushan","Priyati","Prema","Swapnil","Hena","Amey"} #Again assign it because ndrteam got change in above statement
common = fullteam.intersection(ndrteam) #return common element from both set
print("common")
print(common)

ndrteam.intersection_update(fullteam); #put common element in ndrteam ,the difference_update() method removes the unwanted items from the original set
print("common :->")
print(ndrteam)

symetricdiff = ndrteam.symmetric_difference(fullteam) #this method returns a set that contains all items from both set, but not the items that are present in both sets ie symetricdiff = ndrteam U fullteam - ndrteam N fullteam
print("symetricdiff")
print(symetricdiff);

ndrteam.symmetric_difference_update(fullteam) # this  method updates the original set by removing items that are present in both sets, and inserting the other items. ie ndrteam = ndrteam U fullteam - ndrteam N fullteam
print("symetricdiffupdate")
print(ndrteam)

ndrteam = {"Bhushan","Priyati","Prema","Swapnil","Hena","Amey"} #Again assign it because ndrteam got change in above statement
union = ndrteam.union(fullteam); #return combination of both set and suppress duplicate
print("union")
print(union)


flag = ndrteam.isdisjoint(fullteam) #Returns whether two sets have a intersection or not, return false if intersection is there otherwise true
print("disjoint flag")
print(flag)

flag = ndrteam.issubset(fullteam) # this method return true if all element of set present in specified set otherwise false
print("issubset flag")
print(flag)

flag = fullteam.issuperset(ndrteam)#this method return true if all item is present in the specified set otherwise false
print("issupperset flag")
print(flag)


number={9,3,1,2,5,6,8,10,4,7}
print("Length of number :->")
print(len(number)) # it will return length of set number

print("Min element:->")
print(min(number))  # it will return min element from the set

print("Max element:->")
print(max(number))  # it will return max element from the set 

print("Sum element:->")
print(sum(number))  # it will return sum of element of the set

