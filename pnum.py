a = int(input("Enter any number"))
num = a
result = 0
while (a!= 0):
	rem = a%10
	result = result*10+rem
	a = a//10
if(num == result):
	print("Number is palindrome")
else:
	print("Number is not palindrome")