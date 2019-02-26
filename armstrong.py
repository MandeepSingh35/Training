a= input("Enter any number you want to find where the number is Armstrong or not")
n = len(a)
b = int(a)
div =10
j = 0
temp = 0
for i in range (n):
	value = 0
	power = 10 ** j
	value = int((b % div)/power)
	print (value)
	newval = value ** n
	temp += newval
	j = j + 1
	div = div * 10
print (temp)