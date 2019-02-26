value = int(input("Enter any number"))
print("You can choose the base from 2, 16, 8, 10")
base = int(input("Enter any base"))
if (base == 2):
	print(bin(value))
elif (base == 16):
	print(hex(value))
elif (base == 8):
	print(oct(value))
elif (base == 10):
	print(value)
else:
	print("Wrong Input")