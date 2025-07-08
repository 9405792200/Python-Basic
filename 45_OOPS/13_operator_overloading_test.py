class Time:
    def __init__(self,time):
        self.totalsec = time;
        self.hr = time//(60*60)
        self.min=(time-(self.hr*60*60))//60
        self.sec=time-(self.hr*60*60)-(self.min*60)
        
    def display(self,operation):
        print("{0}=> {1}:Hr,{2}:Min,{3}:Sec".format(operation,self.hr,self.min,self.sec))

#------------- Arithmatic operator overloading ---------------------------------
    def __add__(self,other): # operator overloading for + operator
        newtime = Time(self.totalsec + other.totalsec)        
        return newtime 

    def __sub__(self, other):# operator overloading for - operator
        newtime = Time(self.totalsec - other.totalsec)
        return newtime
    
    def __mul__(self, other):# operator overloading for * operator
        newtime = Time(self.totalsec * other.totalsec)
        return newtime
        
    def __truediv__(self, other):# operator overloading for / operator
        newtime = Time(self.totalsec / other.totalsec)
        return newtime
    
    def __floordiv__(self,other):# operator overloading for // operator
        return Time(self.totalsec // other.totalsec)
        
    def __pow__(self,other):#operator overloading for ** operator 
        return Time(self.totalsec ** other.totalsec)

    def __mod__(self,other):#operator overloading for % operator
        return Time(self.totalsec % other.totalsec) 

#---------------------Logical Operator Overloading--------------------------
    def __gt__(self,other):# operator overloading for > operator        
        if self.totalsec > other.totalsec:            
            return True
            
    def __ge__(self,other):# operator overloading for >= operator        
        if self.totalsec >= other.totalsec:
            return True

    def __lt__(self,other):# operator overloading for < operator
        if self.totalsec < other.totalsec:            
            return True
    
    def __le__(self,other):# operator overloading for <= operator
        if self.totalsec <= other.totalsec:            
            return True
     
    def __eq__(self,other):# operator overloading for == operator
        if self.totalsec == other.totalsec:
            return True
            
    def __ne__(self,other):# operator overloading for != operator
        if self.totalsec != other.totalsec:
            return True
     
t1 = Time(6000)
t1.display("Time1")

t2 = Time(9000)
t2.display("Time2")
 
#----------------------Arithmatic Operator --------------------------------------
total = t1 + t2 # total = t1.__add__(t2), t1 go's in self & t2 go's in other
                # internally it will call __add__() method of class Time 
total.display("Add ")

difference= t2 - t1 # difference = t2.__sub__(t1), t2 go's in self & t1 go's in other
                    # internally it will call __sub__() method of class time
difference.display("Subt")

multiplication = t1 * t2 # multiplication = t1.__mul__(t2), t1 go's in self & t2 go's in other 
multiplication.display("Mult") # internally it will call __mul__() method of class time

div = t2 / t1 # div = t2__truediv__(t1), t2 go's in self & t1 go's in other
              # internally it will call __truediv__() method of class time
div.display("Div ")

fdiv=t2 // t1 # fdiv = t2.__floordiv__(t1), t2 go's in self & t1 go's in other
fdiv.display("FDiv")# internally it will call __floordiv__() method of class time

tp1=Time(30)
tp2=Time(10)
power=tp1**tp2 # power = tp1__pow__(tp2),tp1 go's in self & tp2 go's in other
power.display("Pow ")# internally it will call __pow__() method of class Time

mod = t2 % t1 # mod = t2.__mod__(t1), t2 go's in self & t1 go's in other
mod.display("Mod ")# internally it will call __mod__() method of class time

#------------------ Logical Operator Overloading--------------------------
var=t1 > t2 # var = t1.__gt___(t2), t1 go's in self & t2 go's in other
            # internally it will call __gt__() method of class Time
if var:
    print("t1 is > than t2 --1")
else:
    print("t1 is < than t2---1");

#var=t1 >= t2 # var = t1.__ge___(t2), t1 go's in self & t2 go's in other
            # internally it will call __ge__() method of class Time
if var:
    print("t1 is >= to t2---2")
else:
    print("t1 is <= t2---2");
    
var=t1 < t2 # var = t1.__lt___(t2), t1 go's in self & t2 go's in other
            # internally it will call __lt__() method of class Time
if var:
    print("t1 is < than t2---3")
else:
    print("t1 is > than t2---3");
    
var=t1 <= t2 # var = t1.__le___(t2), t1 go's in self & t2 go's in other
            # internally it will call __le__() method of class Time
if var:
    print("t1 is <= than t2---4")
else:
    print("t1 is >= than t2---4");
    
if t1==t2:  #t1.__eq___(t2), t1 go's in self & t2 go's in other
            # internally it will call __eq__() method of class Time
    print("t1 equal to t2")
else:
    print("t1 not equal to t2")
    
if t1!=t2:  #t1.__ne___(t2), t1 go's in self & t2 go's in other
            # internally it will call __ne__() method of class Time
    print("t1 not equal to t2")
else:
    print("t1 equal to t2")