#To handle exception we use try & except block

try:
    a = int(input("Enter Number :"))
    b = int (input("Enter Number:"))
    result = a / b;
    print("{0}/{1} = {2}".format(a,b,result))    
except ValueError as e: # To catch specific exception of type ValueError, occures when input is string
    print("Error!!!Enter Proper Number->",e)
except ZeroDivisionError as e: # To catch specific exception division by zero error
    print("Error!!!Division By Zero->",e)
except Exception as e: # To catch generic error & it should be always last of any specific exception
    print("Generic Error->",e);
else: # This else block will executed when there is no exception raise by try block 
    print("No Exception")
finally: # This finally block will always executed if we get error as well as if we don't get the error
    print("Bye Bye")
