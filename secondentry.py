#x = int(input("Enter the number of elements to be entered: "))
list = [(4,2),(2,9),(3,3),(6,1)]
x = len(list)
#for i in range(0,x):
	#element = int(input("Enter the element: "))
	#list.append(element)
for j in range(0,x):
	for k in range(j,x):
		if(list[j][1] > list[k][1]):
			temp = list[j]
			list[j] = list[k]
			list[k] = temp
		else:
			continue
print(list)
#print("Smallest value is: ",list[0])