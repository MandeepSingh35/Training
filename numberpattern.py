a = int(input("Enter the number till which you want to print"))
for i in range(1,a+1):
	print()
	for j in range(a,i, -1):
		print(" ",end="")
	for k in range(i):
		print(" ",i,end = "")
