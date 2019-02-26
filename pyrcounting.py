a = int(input("Enter the number of stars you want to print"))
n = 1
for i in range(1,a):
	print()
	for j in range(1,i+1):
		print(" ", n,end = "")
		n = n+1