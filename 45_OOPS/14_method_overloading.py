#In python method overloading is not supported. To achive this there are different way by assigning default value to argument 
class Math:
    def add(self,a,b):
        return a + b
    
    def add(self,a=None,b=None,c=None): # to support mehod overloading assign default value to argument, 
                              # above add(self,a,b) method will never call as it is replace by new add(self,a,b,c=None)
        if a!= None and b!= None and c!=None: 
            return a + b + c
        elif a!= None and b!= None:
            return a + b 
        else: 
            return a
    
m1 = Math()
result = m1.add(10,12);
print('Result = {0}'.format(result))
result = m1.add(10,12,20);
print('Result = {0}'.format(result))
result = m1.add(40);
print('Result = {0}'.format(result))
result = m1.add();
print('Result = {0}'.format(result))

