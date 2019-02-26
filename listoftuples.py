a1 = [(4,6),(7,9),(5,1),(4,6),(7,9),(9,6),(9,6),(7,9)]
call = []
x= len(a1)
flag = 0
count=0
#for i in range(0,x):
	#element = int(input("Enter the element: "))
	#list.append(element)
for j in range(0,x):
	for k in range(j+1,x):
		if(a1[j] == a1[k]):
			if(a1[j][1]==a1[k][1]):
				count=count+1
				flag = 0
				break
			#elif(a1[j][1]!=a1[k][1]):
				flag=1
				break
				#call.append(a1[j])
				#print(call)
		elif(a1[j]!=a1[k]):
			flag = 1
			#call.append(a1[j])
	if(flag == 1):
		call.append(a1[j])
#print(a1)
print(call)
print(count)