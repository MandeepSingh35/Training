a = int(input("Enter the number of rows for pattern: "))
for i in range(0,a):
	for j in range(0,a):
		if(i== j):
			print("*",end="")
		elif(i == (a-j-1)):
			print("*",end="")
		else:
			print(" ",end="")
	print()