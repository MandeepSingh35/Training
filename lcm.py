a =int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
k = 0
if(a>b):
	greater = a
else:
	greater = b
for num in range(greater, a*b):
	if(num%a == 0 and num%b == 0):
		print(num)
		break