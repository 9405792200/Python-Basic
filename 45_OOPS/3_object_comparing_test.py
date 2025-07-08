class Time:
    def __init__(self,min,sec): # constructor for class Time
        self.min=min # instance field of class
        self.sec=sec # instance field of class
    
    def compare(self,other):# instance method() of class Time
        if self.sec==other.sec and self.min==other.min:
            return True
        else:
            return False
            
t1=Time(10,12) #t1 object is created on heap
t2=Time(10,12) #t2 object is created on heap

if t1.compare(t2):#t1 object will go in self and t2 object will go in other for compare() method
    print("Same Object")
else:
    print("Different Object")