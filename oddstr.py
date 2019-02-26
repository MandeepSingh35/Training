str = input("Enter the string")
m = len(str)
if(m %2 == 1):
	print(str[::-1])
else:
	print(str)