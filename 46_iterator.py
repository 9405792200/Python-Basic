class generateSequence:
    def __init__(self,start,end):
        self.start = start
        self.end = end

    def __iter__(self): # to get iterable object from iter() method we need __iter__method for object initilization 
                        # & should return iterator object  
        return self

    def __next__(self): # to get next element from sequnce this method is internally call by for loop to get element. 
        x = self.start
        self.start = self.start + 1
        if x > self.end:
           raise StopIteration # this is important to stop iteration otherwise it will be in infinite loop
        return x

seq = generateSequence(10,25)
itSeq = iter(seq) # iter() used to get iterable object for class Seq

for x in itSeq: # internally it will call __next__() method to get element from iterator itSeq
    print(x)

#Note:-> For iterator class should always have __iter__() & __next__() method, otherwise it is not iterator