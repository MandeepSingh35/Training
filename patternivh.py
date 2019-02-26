a = int(input("Enter the number till which you want the numbers: "))
for i in range(0, a+1):
	if(i % 2 == 1):
		print("* "*i)
for i in range(a-2, 0,-1):
	if(i % 2 == 1):
		print("* "*i)