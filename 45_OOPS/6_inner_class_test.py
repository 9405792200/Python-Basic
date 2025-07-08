class Race: #Outer class 
    class Time: #inner class
        def __init__(self, sec): # this is constructor for inner class
            self.sec = sec
        
        def interval(t1,t2):# instance method of class Time
            if t1.sec > t2.sec:
                return t1.sec - t2.sec
            else:
                return t2.sec - t1.sec
        @staticmethod
        def show(sec): # this static method is of class Time
            hr=int(sec/(60*60))
            min=int((sec - (hr*60*60))/60)
            sec=sec - hr*60*60 - min * 60
            print("{0}:Hr,{1}:Min,{2}:Sec".format(hr,min,sec))
        
    def __init__(self,user,distance,time): # this is constructor for outer class
        self.user=user
        self.distance=distance
        self.Time=self.Time(time) # To invoke inner class in outer class 
    
    def show(self):# this instance method is of class Race
        print("Name:{0} Distance:{1} KM Time:{2} Sec".format(self.user, self.distance, self.Time.sec))

bhushan=Race("Bhushan", 2, 845) # to create Race() object
swapnil=Race("Swapnil", 2, 700) # to create Race() object
bhushan.show() # this will call show() method of Race class
Race.Time.show(bhushan.Time.sec)# To call show() static method of inner class Time{outer_class_object.inner_class_name.inner_method_name()}
swapnil.show() # this will call show() method of Race class
Race.Time.show(swapnil.Time.sec)# To call show() static method of inner class Time{outer_class_object.inner_class_name.inner_method_name()}
gap=bhushan.Time.interval(swapnil.Time); # To call interval method of inner class Time {outer_object.inner_class_name.inner_method_name()}
print("Time Interval:->")
Race.Time.show(gap) # To call show() static method of inner class Time{outer_class_name.inner_class_name.inner_method_name()}
