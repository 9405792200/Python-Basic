dataset = [40,20,15,10,100,60,55,33,120,9]
print("Before Sorting ", dataset)

def sort(dataset):
    for index in range(len(dataset)):
        min_index = index;
        minimum = dataset[index]
        for index1 in range(index+1,len(dataset)):
            if (minimum > dataset[index1]):
                minimum = dataset[index1]
                min_index = index1
        
        temp = dataset[index]
        dataset[index] = dataset[min_index]
        dataset[min_index] = temp

sort(dataset)

print("After  Sorting ", dataset)
            
