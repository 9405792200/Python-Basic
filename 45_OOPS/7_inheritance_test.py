class Employee:
    def __init__(self,id,name,numofdays):
        self.id=id
        self.name=name
        self.numofdays=numofdays
    
    def calculateSalary(self):
        self.salary = self.numofdays * 855.56
    
    def showEmployee(self):
        print("ID:{0} Name:{1} Salary:{2}".format(self.id, self.name, self.salary))

class SalesPerson(Employee): #for inheritance (SalesPerson is sub class & Employee is super calss )
    def __init__(self, id,name,numofdays,saleUnit):#sub class init() method, override init() method of super class
        self.saleUnit = saleUnit # saleUnit is attribute of sub class 
        super().__init__(id, name, numofdays) #super() method is used to call super class constructor, 
                                            #it is responsibility of sub class to call constructor of super class because
                                            #at time of object creation of sub class only constructor of sub class get called.
        
    def calculateSalary(self):# it override calculateSalary() method of super() class 
        super().calculateSalary() #To call method of super class use super() method super().super_class_methodname()
        if self.saleUnit > 500:
            self.salary=self.salary + (self.saleUnit - 500)*50
        elif self.saleUnit > 300:
            self.salary=self.salary + (self.saleUnit - 300)*30
        elif self.saleUnit > 100:
            self.salary=self.salary + (self.saleUnit - 100)*10
            
emp1=Employee(1, "Bhushan", 28) # To create employee super class object
emp1.calculateSalary() # To call super class instance method
emp1.showEmployee() # To call super class instance method

sale1=SalesPerson(2,"Swapnil",28,600) # To create salesPerson super class object
sale1.calculateSalary();
sale1.showEmployee()

sale2=SalesPerson(3,"Priyati",28,400)
sale2.calculateSalary();
sale2.showEmployee()

sale3=SalesPerson(4,"Hena   ",28,200)
sale3.calculateSalary()
sale3.showEmployee()

sale4=SalesPerson(5,"Prema  ",28,50)
sale4.calculateSalary()
sale4.showEmployee()