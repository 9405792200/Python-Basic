import threading # this module is used for multithreading 

def printSqure(number):
    for x in range(1,number):
        print("Squre of {0}:{1}".format(x, x * x))

def printCube(number):
    for x in range(1,number):
        print("Cube of {0}:{1}".format(x, x * x * x))

t1 = threading.Thread(target = printSqure, args = (11,)) # To create new thread t1, we created an object of Thread Class, 
                                                         # it takes two arguments, target:->the function to be executed by thread, args:->the arguments to be passed to the target function
t2 = threading.Thread(target = printCube, args = (11,))  # To create new thread t2, we created an object of Thread Class
                                                         # it takes two arguments target:->the function to be executed by thread, args->the arguments to be passed to the target function           

t1.start() # To start execution of thread t1, we use start method of Thread class which will internaly call run() method 
t2.start() # To start execution of thread t2, we use start method of Thread class which will internaly call run() method

t1.join() # We use join() method in order to stop execution of main thread until a t1 thread is complete
t2.join() # We use join() method in order to stop execution of main thread until a t2 thread is complete

print("Bye Bye!!!") # this will execute after t1 & t2 is completed