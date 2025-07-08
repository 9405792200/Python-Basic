possition = 0

def search (dataset, key):
    low = 0
    high = len(dataset) - 1
    mid = (low + high) // 2 # Interger division or floor division
    global possition
    while( low!= high):
        if (key > dataset[mid]):
            low = mid + 1
        else: 
            high = mid 
        mid = (low + high) // 2 # Interger division or floor division
        if (key == dataset[mid]):
            possition = mid + 1
            return True
    return False
    
dataset = [10,20,30,40,50,60,70,80,90,100,110]
key = int(input("Enter Key "))

if search(dataset, key):
    print("key Found At Location",possition)
else:
    print("Key Not Found!!!")