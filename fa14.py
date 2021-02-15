def search(arr,x):
	for i in range (len(arr)):
		if arr[i]==x:
			return i
	return -1	
arr=['h','a','s','i','l']
x="s"
print("element intex:"+str(search(arr,x)))	