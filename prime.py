# your code goes here
n=int(raw_input("Enter the number"))
prime=1
i=2
while(i<n):
	if(n%i==0):
		prime=0
	i=i+1
if(prime==1):
	print("It is a prime number")
else:
	print("it is not a prime number")
		
