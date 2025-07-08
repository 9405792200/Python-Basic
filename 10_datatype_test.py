print("Interger Type")
num = 10
print(num)
print(type(num))
print("-------------------------")

print("Float Type")
num = 10.11
print(num)
print(type(num))
print("-------------------------")

print("complex Type")
num = 9 + 8j
print(num)
print(type(num))
print("-------------------------")

print("Boolean Type");
flag = 4 < 5
print(flag)
print(type(flag))
print("-------------------------")

flag = 4 > 5
print(flag)
print(type(flag ))
print("-------------------------")

print("List Type")
num = [10,20,40,50]
print(num)
print(type(num))
print("-------------------------")

print("Tuple Type")
num = (10,20,40,50)
print(num)
print(type(num))
print("-------------------------")

print("Set Type")
num = {10,20,40,50}
print(num)
print(type(num))
print("-------------------------")

print("String Type")
name = "Bhushan"
print(name)
print(type(name))
print("-------------------------")

print("Range Type")
num = range(5) # it generate sequence 
print(num)
print(type(num))

num = list(range(10)) # it generate list start from zero by default , end at 10 (excluded), by default incerement by 1
print(num);

num = list(range(1,10,2)) # it generate list start from 1 end at 10 (excluded) incerement by 2 o/p is [1,3,5,7,9]
print(num)

num = list(range(9,-1,-2)) # it generate list start from 10 end at -1 (excluded) decrement by 2 o/p is [9,7,5,3,1]
print(num)
print("-------------------------")

data = {1:"Bhushan", 2:"Priyati", 3:"Hena"}
print(data)
print(type(data))
print("-------------------------")
