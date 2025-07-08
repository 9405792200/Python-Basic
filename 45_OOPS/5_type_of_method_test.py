class Time:
    objectcount=0 #this is class/static variable, This variable common for all object
    
    def __init__(self,time):# special method __init__(self) is same as constuctor which is called at time of object creation
        self.hr=int(time/(60*60))
        self.min=int((time - (self.hr*60*60))/60)
        self.sec=time - self.hr*60*60 - self.min * 60
        Time.objectcount=Time.objectcount+1 #To invoke class/static variable use class_name.variable_name
        
    def displayTime(self): # this is instance method called on object hence take self as parameter
        print("{0}:Hr,{1}:Min,{2}:Sec".format(self.hr,self.min,self.sec)) #hr min & sec are instance variable
        
    @classmethod
    def totalTimeObject(cls): # this is class method called on class hence take cls as parameter
        return cls.objectcount # to access class variable
        
    @staticmethod
    def welcomeMessage(username):
        print("WelCome To Time Converter {0}".format(username))
        
Time.welcomeMessage("Bhushan");
sec=int(input("Enter Time:"))
for x in range(1,6,1):
    t=Time(sec*x)   # here __init__() method call with parameter sec, memory allocation is in heap section
    t.displayTime() # instance method called on object t

count=Time.totalTimeObject()
    
print("Total Time Object:{0}".format(count))
