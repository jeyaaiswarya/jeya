
a=input("Enter the number")
b=input("number to be raised")
if(a.isnumeric()):
    a=int(a)
    if(b.isnumeric()):
        b=int(b)
        c=a**b
        print(c)
    else:
        print("The number  entered is invalid")
else:
    print("The number  entered is invalid")
    
	


