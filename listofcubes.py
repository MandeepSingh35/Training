list1 = []
a = int(input("Enter the number of elements to be entered: "))
for i in range(0,a):
	element = int(input("Enter the number: "))
	list1.append(element)
list3 = []
for i in list1:
	t1 = (i,i**3)
	list3.append(t1)

print(list3) 