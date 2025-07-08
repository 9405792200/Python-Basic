def count_even_odd(values):
    even_count = 0
    odd_count = 0
    
    for value in values:
        if value % 2 == 0:
            even_count = even_count + 1
        else:
            odd_count = odd_count + 1
            
    return even_count, odd_count # return multiple values


data_set = []
choice = 'Y'
while choice == 'Y':
    val = int(input("Enter Number:"))
    data_set.append(val)
    choice = input("DO you want to continue(Y/N)?")[0]
    
even, odd = count_even_odd(data_set) # passing list to a function count_even_odd

print(data_set)
print("Even count: {0} and odd count: {1}".format(even, odd)) # here on string we can use format() method direct