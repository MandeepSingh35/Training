n = int(input("Enter the number till which you want to print prime numbers: "))
print("All prime numbers are: ")
for a in range(2, n+1):
	k = 0
	for j in range(2, a):
		if (a % j == 0):
			k = 1
			break
		
	if(k != 1):
		print(a)