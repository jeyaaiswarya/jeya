n1=int(input("Enter the number"))
d1=0
while(n1>0):
	r1=n1%10
	d1=d1*10+r1
	n1=n1//10
print(d1)
