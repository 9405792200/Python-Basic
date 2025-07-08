from abc import ABC,abstractmethod

class Shape(ABC): #To create abstract class inherit ABC class and apply decorater @abstractmethod on method to make it abstract
    def __init__(self, name):
        self.name = name 
    
    @abstractmethod    
    def calculateArea(self): # this is abstract method because of decorater abstractmethod is applied on method
        pass
    
    def displayArea(self,area):
        print("Area Of Shape {0} = {1}".format(self.name, area));

class Triangle(Shape): # here need to implement calculateArea() method because 
                       # if we not implement then this class will again abstract class
    def calculateArea(self,base,height):# Overridet abstract method
        return 1/2 * base * height

class Squre(Shape):
    def calculateArea(self,length):# Overridet abstract method
        return length * length;
    
t1 = Triangle("Triangle")
area = t1.calculateArea(4,5)  
t1.displayArea(area) 

s1 = Squre("Squre")
area = s1.calculateArea(5);
s1.displayArea(area);    

# Note :-> We can not create object of abstract class & abstract class should have atlist one abstract method