def cube(num):      # user define module can contain function() 
    return num * num * num
    
PI=3.14 #User define module can contain variable of all types

def fibo(num): # user define function inside module my_math
    result=[]
    a , b = 0,1
    
    while a < num:
        result.append(a)
        a ,b = b,a+b
        
    return result

