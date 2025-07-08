#Type of argument in python
#1)position argument
#2)default argument
#3)keyword argument
#4)variable length argument
#5)keyworded variable length argument

def calculateAmount(pamount, time, rate = 6.5):
    interest = pamount * time * rate / 100
    return interest
    
str = "Principle Amount={0} Interest Amount={1} Total={2}"

principle = float(input("Enter Principle Amount:"))
duration = float(input("Enter Duration:"))

interest = calculateAmount(principle, duration, 7.5) #Example of positional argument
print(str.format(principle, interest, principle + interest))

interest = calculateAmount(principle, duration) #Example of default argument, here rate is 6.5 that is default value define in calculateAmount() function
print(str.format(principle, interest, principle + interest))

interest = calculateAmount(time = duration, rate = 8, pamount = principle) #Example of keyword argument, parameter will be passed parameter_name = value
print(str.format(principle, interest, principle + interest))

#for argument type 4th and 5th refer next program