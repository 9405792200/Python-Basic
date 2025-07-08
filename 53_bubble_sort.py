def sort(dataset):    
    for iteration in range(len(dataset),0,-1): # this is just for number of pass       
        for index in range(iteration - 1):
            if (dataset[index] > dataset[index + 1]):
                temp = dataset[index] # below is swapping logic
                dataset[index] = dataset[index + 1]
                dataset[index + 1] = temp

dataset = [99,88,66,77,30,55,40,10,5,990]

sort(dataset)
print(dataset)
