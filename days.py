day=input()
holiday=("Saturday","Sunday")
working=("Monday","Tuesday","Wednesday","Thursday","Friday")
if day in holiday:
	print("It is a holiday")
elif day in working:
	print("It is a working day.")
else:
	print("Enter a valid day")
