age = int(input("Enter age :"))

if age > 0 and age <= 13:
    print("Child")
elif age >= 14 and age <= 18:
    print("Teen")
elif age >= 19 and age <= 55:
    print("Adult")
elif age >= 56 and age <= 100:
    print("Senior Citizen")
else:
    print("Invalid Age")