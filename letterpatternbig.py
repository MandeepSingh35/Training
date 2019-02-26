a = input("Enter the alphabet till you have to go: ")
b = ord(a)
print("		",b,"		")
for i in range(97,b+1):
	print()
	for j in range(b+1, i, -1):
		print(" ",end="  ")
	for k in range(97,i+1):
		print(" ",chr(k),end = "")
	for l in range(i-1,96,-1):
		print(" ",chr(l), end ="")
			
