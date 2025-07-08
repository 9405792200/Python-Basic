source = open('sample.txt','r') # to open file we use open() function there are different mode to open file 
                                # r,rb,r+,rb+ | w,wb,w+,wb+ | a,ab,a+,ab+
destination = open('samplecopy.txt','w')

for line in source: #To read each individual line from source file
    print(line,end='')
    destination.write(line)  #To write line data to destination file 

#print(source.read()) # To read full file at once 
#print(source.read(5)) # To read first 5 character of file 
   
source.close()  # To close source file 
destination.close() # To close destination file
print('\nBye Bye')
