a = input("Enter any String: ")
j = len(a)
for i in range(1,j):
	if(a[i]>= chr(96) and a[i]<=chr(122)):
		print(a[i], end="")