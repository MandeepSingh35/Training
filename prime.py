num = int(input("Enter the number to find whether"))
f = 0
for i in range(2,num):
	if((num % i) == 0):
		f = 1
		break
	else:
		f = 0
		break
if(f == 1):
	print("Number is not prime")
else:
	print("Number is prime")