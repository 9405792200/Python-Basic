import threading 

balance = 0
lock = threading.Lock(); #threading module provide Lock class to deal with race condition i.e to handle race condition 

def deposite(amount):
    global balance
    for index in range(1000000):        
        lock.acquire() # To take lock 
        balance = balance + amount #this is critical section of program put then in lock acquire & release
        lock.release() # To release lock
        
def withdraw(amount):
    global balance
    for index in range(500000): 
        lock.acquire() # To take lock
        balance = balance - amount #this is critical section of program put then in lock acquire & release
        lock.release() # To release lock

jack=threading.Thread(target=deposite,args=(1,)) #To create thread object
jill=threading.Thread(target=withdraw,args=(1,)) #To create thread object

jack.start()# To start execution of thread
jill.start()# To start execution of thread

jack.join() #in order to stop execution of main thread until a jack thread is complete
jill.join() #in order to stop execution of main thread until a jill thread is complete

print("Final Balance==> {0}".format(balance))