class Time: # here Time is class
    def getTime(self,time):#getTime()is method of a class, method always contain self as a parameter, same as this pointer in C++
        hr = int(time/(60*60))
        min=int((time-(hr*60*60))/60)
        sec=time-(hr*60*60)-(min*60)
        return hr,min,sec #multiple value return in form of tuple from function getTime()

sec=int(input("Enter Time:"))

t1=Time();#object t1 is created for class Time, memory allocation is in heap section
result=t1.getTime(sec);#method getTime() called on object t1
print("{0}:Hr,{1}:Min,{2}:Sec".format(result[0],result[1],result[2]))
 
print(type(t1))