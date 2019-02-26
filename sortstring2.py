a = input("Enter any string: ")
j = len(a)
temp = 0
b = 0
c = 0
for i in range(0,j):
	if(a[i-1] > a[i]):
		a.replace(a[i-1], a[i])
		temp = ord(a[i])
		#b = ord(a[i+1])
		a[i] = a[i+1]
		#a[i+1] = int(temp)
		print(a[i])
		print(chr(b))
	elif(a[i-1] == a[i]):
		continue
	else:
		continue	
