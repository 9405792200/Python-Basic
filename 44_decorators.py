def div(a,b):
	return a/b

def smart_div(func): # here smart_div is decorators for div function they add extra feature to div() function
    if b==0:
        print("Division By Zero Error")
        return
    else:
        return func(a,b)

a=int(input("Enter Number="))
b=int(input("Enter Number="))

result=smart_div(div)
if result is not None:
    print("{0}/{1}={2}".format(a,b,result))