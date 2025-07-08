def fibonacci(num):
    if num <= 0:
        return
    a = 0
    b = 1    
    
    if num == 1:
        print("{0},".format(a), end="")
    else:
        print("{0},".format(a), end="")
        print("{0},".format(b), end="")

    for x in range(2,num):
        sum = a + b;
        print("{0},".format(sum), end="")
        a = b;
        b = sum
        
fibonacci(20)