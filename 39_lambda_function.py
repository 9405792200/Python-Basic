#lambda function also called anonymous function
#lambda function are small
#lambda function can take n number of argument i.e any number of argument but can only have single expression
#syntax for lambda function is:-> lambda argument : expression

simpleinterest = lambda p, n, r : p * n * r / 100 #lambda/anonymous function which take three argument & has single expression
    #in python function are object here simpleinterest represent anonymous function reference
    
principleamount = float(input("Enter amount :"))
year = int(input("Enter Duration in year :"))

interest = simpleinterest(principleamount, year, 6.5)
print("Total Return Amount : {0}".format(principleamount + interest))