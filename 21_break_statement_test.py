key = [10,5,4,3,9,8,1,7,2,6]

my_key = int(input("Entey key :"))
index = 0

while index < len(key):
    if my_key == key[index]:
        print("Key found at index:", index)
        break; # this will terminate while loop
    index = index + 1

if index == len(key):
    print("Key Not Found")