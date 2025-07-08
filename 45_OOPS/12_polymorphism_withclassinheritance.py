class Employee:
    def __init__(self, name, id, numofdays):
        self.name = name
        self.id = id
        self.numofdays = numofdays
        
    def calculatesalary(self):
        self.salary = self.numofdays * 855.50
        
    def display(self):
        print("ID:{0} Name:{1} Salary:{2}".format(self.id, self.name, self.salary))
        
class SalesPerson(Employee):
    def __init__(self, name, id, numofdays, salesunit):
        super().__init__(name, id, numofdays) # to call super class init() method
        self.salesunit = salesunit
        
    def calculatesalary(self): # this is class inheritance polymorphism, here  calculatesalary of Employee class override by SalesPerson class 
        super().calculatesalary() # to call super class calculatesalary() method
        if self.salesunit > 500:
            self.salary=self.salary + (self.salesunit - 500)*50
        elif self.salesunit > 300:
            self.salary=self.salary + (self.salesunit - 300)*30
        elif self.salesunit > 100:
            self.salary=self.salary + (self.salesunit - 100)*10
            
bhushan = Employee("Bhushan", 1, 28);
bhushan.calculatesalary()
bhushan.display()
    
swapnil = SalesPerson("Swapnil", 2, 28, 1000)
swapnil.calculatesalary()
swapnil.display()