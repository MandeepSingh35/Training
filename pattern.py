a = int(input("Enter the number of stars you want to print: "))
k = 2
for i in range(2, a+1):
	for j in range(2, i):
		for m in range(2,i):
			if ((j % m) != 0):
				k = 1
				break	
			elif((j%m) == 0):
				#print(i,end = "")
				k = 0
				break
		if(k == 1):
			print(" ",j,end = "")
			#break
		elif(k == 0):
			#print(end = "")
			pass
	#k+=1
	print()