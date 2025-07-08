import sys # for command line argument
 
sum = 0
#in sys.argv zeroth index always contains file name
print(sys.argv[0]) # it will print file name 
for index in range(1, len(sys.argv)): # len(sys.argv) retun total number of element in command line argument including file name at zeroth index
    sum = sum + int(sys.argv[index]) # sys.argv[index] return element of mentioned  index
print(sum)

