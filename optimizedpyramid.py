print("Enter the number of stars you want at the last row")
a = int(input("Enter the number of stars you want to print"))
for i in range(1,a+1):
	print()
	for j in range(a, 0, -1):
		if(j>i):
			print(" ",end ="")
		elif(j == i):
			if((j%2)!=0):
				print(" *"*i, end="")
				break
			break