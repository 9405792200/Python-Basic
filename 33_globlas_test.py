age = 30 # global variable age  

def print_age():
    age = 40 # here age is local variable & first precedence is given for local variable
    print("In function age:", age) # here local variable age will print
    age = globals()['age'] # to access global variable age use function globals() to get value of age
    print("In function age:", age)
    globals()['age'] = 50
    
print_age() # function call to print_age
print("Outside function age:", age)