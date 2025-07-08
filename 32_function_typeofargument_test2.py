#example of variale length argument function
def sum(*values): # here values is tuple which hold value of passed argument to function sum(). here * is variale length argument
    sum = 0
    for x in values:
        sum = sum + x
    return sum
    

result = sum(1,5,6,8,9,10) # function call to sum()
print("result:",result)

#example of keyworded variale length argument function
def person(**value): # here values is dictionary which hold value of passed argument to function person, here ** is keyworded variale length argument 
    print("Name :",value["name"]);
    print("Age :",value["age"]);
    print("Contact :",value["contact"]);
    
person(age="26", contact="9405792200", name="Bhushan") # function call to person()