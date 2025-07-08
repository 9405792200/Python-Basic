import sys

limit = sys.getrecursionlimit() # this function is define in sys module to get recursion limit
print(limit)
sys.setrecursionlimit(2000) # to set recursion limit, by default recursion limit is 1000
count = 0


def greet():
    globals()['count'] = globals()['count'] + 1
    print(count)
    print("Welcome")
    greet() # function calling itself 

    
greet()
