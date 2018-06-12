n=int(input("Enter the number"))
d=0
while(n>0):
	r=n%10
	d=d*10+r
	n=n//10
print(d)
