def bubblesort(nlist):
	for passnum in range(len(nlist)-1,0,-1):
		for i in range(passnum):
			if nlist[i]>nlist[i+1]:
				temp=nlist[i]
				nlist[i]=nlist[i+1]
				nlist[i+1]=temp
nlist=[54,65,63,87,95,64]
bubblesort(nlist)
print(nlist)				