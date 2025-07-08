print("numbers list:->");
numbers = [10,20,30,40,50,60,70,80,90,100]
print(numbers)          # it print full list
print(numbers[0])       #it print element at index zeop o/p 10
print(numbers[2:5])     #it print element start from index 2 and end at index 5,here second parameter is exclusive o/p [30,40,50]
print(numbers[:5])      #it print element start from index zero to index 5 (exclusive) o/p [10,20,30,40,50]
print(numbers[3:])      #it print element start from index 3 to end o/p [40,50,60,70,80,90,100]
print(numbers[4:90])    #it print element start from index 4 to end o/p [50,60,70,80,90,100]
print(numbers[-4])      #it print 4th element from last o/p 70
print(numbers[-3:])     #it print element start from last 3rd to end o/p [80,90,100]
print(numbers[-4:-1])   #it print element start from last 4th to -1 (exclusive) o/p [70,80,90]
print(numbers[-4:-8])   #it will return empty list because indexing always move from left to right  o/p[]
print("--------------------------------------------------------")

print("names list:->")
names = ["Bhushan","Swapnil","Prema","Priyati","Hena"]
print(names)
print(names[0])       #it print element at index zero 
print(names[2:5])     #it print element start from index 2 and end at index 5,here second parameter is exclusive 
print(names[:5])      #it print element start from index zero to index 5 (exclusive) 
print(names[3:])      #it print element start from index 3 to end 
print(names[4:90])    #it print element start from index 4 to end 
print(names[-4])      #it print 4th element from last 
print(names[-3:])     #it print element start from last 3rd to end 
print(names[-4:-1])   #it print element start from last 4th to -1 (exclusive) 
print(names[-4:-8])   #it will return empty list because indexing always move from left to right  o/p[]
print("--------------------------------------------------------")

print("value list:->")
values=['Bhushan',26,'Priyati',30,'Prema',35.66]
print(values)
print(values[0])       #it print element at index zero 
print(values[2:5])     #it print element start from index 2 and end at index 5,here second parameter is exclusive 
print(values[:5])      #it print element start from index zero to index 5 (exclusive) 
print(values[3:])      #it print element start from index 3 to end 
print(values[4:90])    #it print element start from index 4 to end 
print(values[-4])      #it print 4th element from last 
print(values[-3:])     #it print element start from last 3rd to end 
print(values[-4:-1])   #it print element start from last 4th to -1 (exclusive) 
print(values[-4:-8])   #it will return empty list because indexing always move from left to right  o/p[]
print("--------------------------------------------------------")

print("combination of list")
combine=[numbers,names]
print(combine)
print(combine[0])   #it print first list that is numbers list
print(combine[1])   #it print second list that is names list
print(combine[-2]); #it print second list from last that is numbers list
print(combine[-1]); #it print first list from last that is names list

print(combine[0][0]) #it print first element of first list
print(combine[1][0]) #it print first element of second list

print(combine[0][-3]) #it print last 3rd element from first list that is from numbers
print(combine[1][-2]) #it print lasrt 2nd element from second list that is from names