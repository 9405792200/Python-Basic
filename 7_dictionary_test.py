contact={"Bhushan":9405792200, "Paramjeet":9004646727, "Mummy":9422256790,"Home":"02588-245000"}
print(contact)

value=contact["Home"];# To get value of key "Home"
print(value) 

#value=contact["Poonam"] #This is KeyError because Poonam key is not in contact dictionary
#print(value)

contact["Poonam"] = 8180041699 # To add element in contact dictionary
print(contact)

contact["Paramjeet"]=7276895231 #To change the value for key Paramjeet
print(contact)

name=["Bhushan","Poonam","Mummy"]
profile=["Private Job","House wife","Government Job"]
data = dict(zip(name, profile)) # It will combine two list in the form of key value pair to create new dictionary data
print(data)

#Example of nested dictionary
nested_disc = {"Child1":{"name":"Mamta","age":35}, 
               "Child2":{"name":"Archana", "age":33},
               "Child3":{"name":"Bhushan", "age":28}
               }
print(nested_disc)
print(nested_disc["Child1"]) # To print value of key Child1
print(nested_disc["Child2"]) # To print value of key Child2
print(nested_disc["Child3"]) # To print value of key Child3

print(nested_disc["Child1"]["name"]) # It return value of key name of child1 dictionary
print(nested_disc["Child1"]["age"])  # It return value of key age of child1 dictionary