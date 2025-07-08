def generateSequnce(start,end):    
    while( start <= end ):
        yield start;  # yield is special keyword, 
                      # diffrence between return and yield they both return value but in yield executaion of function is continue   
                      # because of yield keyword generateSequnce() is not simple function it is generater function     
        start = start + 1        

values = generateSequnce(1,15) #because of yield keyword generateSequnce() return generator object
#There are two way to access generator object
#1)Using for loop on generater object
#2)Using next() method on generater object

print(next(values))

for x in values:
    print(x)
    
