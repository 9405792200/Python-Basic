key = [10,5,4,3,9,8,1,7,2,6]

my_key = int(input("Entey key :"))
index = 0

for x in key:
    if my_key == x:
        print("Key found")
        break; # this will terminate for loop.        
else: # this else block will be executed when the loop is finished
    print("key not found");