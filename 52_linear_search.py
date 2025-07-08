index = 0
def search(dataset, key):
    for x in dataset:
        global index 
        index = index + 1
        if key == x:
           return True
    return False

dataset=[10,20,30,40,55,66,77,88,99,110]
key=int(input("Enter Key "))

if search(dataset, key):
    print("Key Found At Location {0}".format(index))
else:
    print("Key Not Found!!!");