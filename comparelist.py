list1 = []
list2 = []
a = int(input("Enter the number of elements you want to insert: "))
for i in range(0,a):
	element = int(input("Enter the element: "))
	list1.append(element)
print(list1)
num = int(input("Enter the number which you want to compare: "))
for i in list1:
	if(i < num):
		list2.append(i)

print(list2)