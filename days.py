day=input()
holiday=("Saturday","Sunday")
working=("Monday","Tuesday","Wednesday","Thursday","Friday")
if day in holiday:
	print("yes")
elif day in working:
	print("no")
else:
	print("Enter a valid day")
