class Employee:
    def __init__(self, name, id, numofdays):
        self.name = name
        self.id  = id
        self.numofdays = numofdays

    def calculateSalary(self):
        self.salary = round(self.numofdays * 856.55,2)
    
    def showEmployee(self):
        print("ID:{0} Name:{1} Salary:{2}".format(self.id, self.name, self.salary))
        
class SalePerson(Employee):
    def __init__(self, name, id, numofdays, saleunit):
        self.saleunit = saleunit
        super().__init__(name, id, numofdays)
    
    def calculateSalary(self):
        super().calculateSalary()
        if self.saleunit > 500:
            self.salary=self.salary + (self.saleunit - 500)*50
        elif self.saleunit > 300:
            self.salary=self.salary + (self.saleunit - 300)*30
        elif self.saleunit > 100:
            self.salary=self.salary + (self.saleunit - 100)*10

emp1=Employee("Bhushan",1,28)
emp1.calculateSalary()
emp1.showEmployee()

sale1=SalePerson("Swapnil",2,28,1000)
sale1.calculateSalary()
sale1.showEmployee()

flag=isinstance(emp1,Employee) # isinstance() method return True if object is of mentioned type in second parameter
print("Bhushan is Employee :{0}".format(flag))

flag=isinstance(sale1,Employee) # isinstance() method return True if object is of mentioned type in second parameter
print("Swapnil is Employee :{0}".format(flag)) 

flag=isinstance(emp1,SalePerson) # isinstance() method return True if object is of mentioned type in second parameter
print("Bhushan is SalePerson :{0}".format(flag))

flag=isinstance(sale1,SalePerson) # isinstance() method return True if object is of mentioned type in second parameter
print("Swapnil is SalePerson :{0}".format(flag))

flag=issubclass(Employee,SalePerson) #issubclass() method return True if first argument is subclass of second argument
print("Class Employee is Subclass Of SalePerson Class :{0}".format(flag)); 

flag=issubclass(SalePerson,Employee) #issubclass() method return True if first argument is subclass of second argument
print("Class SalePerson is Subclass Of Employee Class :{0}".format(flag)); 