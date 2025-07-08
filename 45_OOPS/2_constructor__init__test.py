class Time:
    def __init__(self,time):# special method __init__(self) is same as constuctor which is called at time of object creation
        self.hr=int(time/(60*60))
        self.min=int((time - (self.hr*60*60))/60)
        self.sec=time - self.hr*60*60 - self.min * 60

    def displayTime(self):
        print("{0}:Hr,{1}:Min,{2}:Sec".format(self.hr,self.min,self.sec)) #hr min & sec are instance variable

sec=int(input("Enter Time:"))
t1=Time(sec) # here __init__() method call with parameter sec, memory allocation is in heap section
t1.displayTime()
