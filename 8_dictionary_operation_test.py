contact={"Bhushan":9405792200, "Paramjeet":9004646727, "Mummy":9422256790,"Home":"02588-245000"}
print(contact)

value = contact.get("Bhushan") # Return value for key "Bhushan"
print(value)

value = contact.get("Poonam") # It will return None because "Poonam" key is not present in contact dictionary
print(value)

value = contact.get("Poonam","Key Not Found") #It will return "Key Not found" string as Poonam key is not present in contact dictionary 
print(value)

contact_bkp = contact.copy() # To copy() dictionary contact to contact_bkp
print(contact_bkp)

contact.clear() # To remove all the elements from the dictionary contact
print(contact)

contact = contact_bkp.copy();

value = contact.pop("Paramjeet") # This method remove specified item from the dictionary, if Paramjeet key is not present in the contact dictionary then it return keyError
print(value)
print(contact)

value = contact.pop("Poonam", "Key not found") # It will try to remove element with key Poonam from contact dictionary, if key poonam not present then it will return "Key not found string"
print(value)

value = contact.popitem() # it will remove last inserted item from the dictionary, and return tuple for removed element 
print(value)

contact.update({"Poonam":85789625}) # This method insert specified item to the dictionary
print(contact)

value=contact.setdefault("Bhushan",81828384); # It will return the value of specified key, If the key does not exist, insert the key, with the specified value, here it will return 9405792200
print(value)

value=contact.setdefault("Ranjeet",81828384); # It will return the value of specified key, If the key does not exist, insert the key, with the specified value
print(contact)

value = contact.items() # Return a view object containig list having tuple for each key value pair
print(value)

key = contact.keys() #Return a view object. The view object contain the keys of dictionary inside list 
print(key)

value = contact.values() #Return a view object. The view object contain the values of dictionary inside list.
print(value)

teamlist = ["Bhushan","Priyati","Prema","Hena","Swapnil"]
team = ["NDR","CTAX","HB"] 
value = dict.fromkeys(teamlist, team) #Return a dictionary with a specified keys & values here teamlist member is key & team list member is value for each key
print(value)

value = len(contact)
print(value)

value = min(contact)
print(value)

value = max(contact)
print(value)