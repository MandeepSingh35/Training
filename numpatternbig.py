a = int(input("Enter the number of stars you want to print: "))
for i in range(1,a+1):
	print()
	for j in range(a, i, -1):
		print(" ",end="")
	for k in range(1,i+1):
		print(k,end = "")
	for l in range(i-1,0,-1):
		print(l, end ="")
			
