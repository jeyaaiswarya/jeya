num=int(raw_input("Enter the number"))
n1=num
n=0
while(num>0):
        d=num%10
        n=n*10+d
        num=num/10
if(n==n1):
        print("It is a palindrome")
else:
        print("It is  not a palindrome")
        
