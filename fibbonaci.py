n = int(input("Enter the number till we have to go"))
i = 0
j = 1
temp = 0
print (i, end = " ")
print(j, end = " ")
for k in range(3, n+1):
	sum = (i + j)
	print (sum, end =" ")
	i = j
	j = sum