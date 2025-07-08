class Shape:
    def __init__(self,shapename):
        self.shapename=shapename
        self.area=0
     
    def show(self):
        print("Area of {0} = {1} unit^2".format(self.shapename,self.area))

class Triangle(Shape): #Example of Single level inheritance,because class Triagle derived from single class shape
    def __init__(self, base, height):
        self.base=base
        self.height=height
        super().__init__("Triagle") # To call constructor of super class
    
    def calculateArea(self):#instance method of class Triagle
        self.area= 1/2 * self.base * self.height

class Rectangle(Shape):#Example of Single level inheritance,because class Rectangle derived from class shape,
                       #from shape class perspective it is herarchical inheritance because shape class is parent of Triagle class & Rectangle class 
    def __init__(self, legth, width,shapename):
        self.legth=legth
        self.width=width
        super().__init__(shapename)#To call constructor of super class

    def calculateArea(self):#instance method of class Rectangle
        self.area=self.legth * self.width

class Squre(Rectangle,Shape):#Example of multiple inheritance,because class Squre derived from class Rectangle & Shape
    
    def __init__(self,legth):
        super().__init__(legth,legth,"Squre") #To call constructor of super class, 
                                      #here there are two super classes but only constructor of Rectangle get called as per ,
                                      #MRO(Method Resolution Order) Rule
                                      #MRO rule work from left to right on class, 
                                      #as Class Squre derived from (Rectangle,Shape) in this syntax Rectangle is on left side hence __init__() method of Rectangle call
                                      
        Shape.__init__(self,"Squre")  #to call __init__() method of another super class, class_name.__init__(self,_,_)
                                      #due to MRO Rule __init__() method of another super class not get called,by above way we can called  
                                      
    def calculateArea(self):
        super().calculateArea()

class Parallelogram(Rectangle):#Example of multilevel inheritance,because class Parallelogram inherited from class Rectangle and Rectangle class inherited from class shape
    
    def __init__(self, base, height,shapename):
        super().__init__(base,height,shapename)

    def calculateArea(self):
        super().calculateArea()
        
t1=Triangle(4,8) #To create Triagle object
t1.calculateArea()#To call instance method
t1.show()

r1=Rectangle(4,8,"Rectangle")#To create Rectangle object
r1.calculateArea()#To call instance method
r1.show()

s1=Squre(4)#To create Squre object
s1.calculateArea()#To call instance method
s1.show()

p1=Parallelogram(4,8,"Parallelogram")#To create Parallelogram object
p1.calculateArea()#To call instance method
p1.show()