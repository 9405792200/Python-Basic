class Employee:
    def __init__(self,name,wday,pdayamount):
        self.name = name
        self.day = wday
        self.pdayamount = pdayamount

    def calculatesalary(self):
        return self.day * self.pdayamount
        

class SalesPerson(Employee):
    def __init__(self,name,wday,pdayamount,saleunit):
        super().__init__(name,wday,pdayamount);
        self.saleunit = saleunit;
    
    def calculatesalary(self):   # This is method overriding, this will override calculatesalary() method of base class 
        salary = super().calculatesalary();
        salary = salary + self.saleunit * 50;
        return salary;
        
emp1 = Employee('Bhushan', 23, 600); #object of Employee class 
salary = emp1.calculatesalary()      # 
print("Salary Of Employee {0} = {1}".format(emp1.name,salary))

sel1 = SalesPerson('Swapnil', 23, 600,50); # object of SalesPerson class 
salary = sel1.calculatesalary()
print("Salary Of Employee {0} = {1}".format(sel1.name,salary))