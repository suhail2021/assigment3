def fibonocci(n):
	if n<0:
		print("incorrect input")
	elif n==0:
		return 0
	elif n==1 or n==2:
		return 1
	else:
	 	return fibonocci(n-1) + fibonocci(n-2)
print (fibonocci(8))	 	
