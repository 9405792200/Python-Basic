def add(x, y): # here function return single value
    z = x + y
    return z
    
def calculateSimpleInterest (p, n, r): # here function return multiple value in form of tuple.In python function can return multiple value 
    simpleInterest = p * n * r / 100;
    return simpleInterest, r  # here function return two values simpleInterest and r
    
result = add(4, 6) # function call in python , here result will hold value of z return by add() function
print(result)

principleAmount = float(input("Enter Amount:"))
year = float(input("Enter Duration in year:"))

str = "{0} Principle amount ={1}, Interest amount ={2}, Total Amount ={3} for Rate ={4}"
silverInterest, silverRate = calculateSimpleInterest(principleAmount, year, 6.5) # function call in python, 
                                                    # here silverInterest will hold value of simpleInterest return by calculateSimpleInterest() function
                                                    # here silverRate will hold value of r return by calculateSimpleInterest() function
goldInterest, goldRate = calculateSimpleInterest(principleAmount, year, 7) # function call in python
                                                    # here goldInterest will hold value of simpleInterest return by calculateSimpleInterest function
                                                    # here goldRate will hold value of r return by calculateSimpleInterest() function
                                                    
print(str.format("As Per Silver Scheme:->", principleAmount, silverInterest, principleAmount + silverInterest ,silverRate))
print(str.format("As Per Gold Scheme  :->", principleAmount, goldInterest, principleAmount + goldInterest ,goldRate))
