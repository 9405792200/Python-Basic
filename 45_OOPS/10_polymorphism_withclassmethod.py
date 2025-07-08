class Employee:
    def __init__(self,name,id,numofdays):
        self.name = name
        self.id = id
        self.numofdays = numofdays
        
    def calculatesalary(self):
        self.salary = self.numofdays * 855.56
        
    def display(self):
        print("ID:{0} Name:{1} Salary:{2}".format(self.id, self.name, self.salary))

class SalesPerson:
    def __init__(self,name,id,numofdays,saleunit):
        self.name = name 
        self.id = id 
        self.numofdays = numofdays
        self.saleunit = saleunit

    def calculatesalary(self):
        self.salary = self.numofdays * 855.56
        if self.saleunit > 500:
            self.salary=self.salary + (self.saleunit - 500)*50
        elif self.saleunit > 300:
            self.salary=self.salary + (self.saleunit - 300)*30
        elif self.saleunit > 100:
            self.salary=self.salary + (self.saleunit - 100)*10

    def display(self):
        print("ID:{0} Name:{1} SaleUnit:{2} Salary:{3}".format(self.id, self.name, self.saleunit, self.salary))
        
bhushan = Employee("Bhushan",1,28)
swapnil = SalesPerson("Swapnil",2,28,1000)

for emp in (bhushan,swapnil): # this is polymorphism with classmethod, because both classes contain same method with same name
    emp.calculatesalary() 
    emp.display()