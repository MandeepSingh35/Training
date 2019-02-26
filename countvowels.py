a = input("Enter the String: ")
j = len(a)
count = 0
for i in range(0,j):
	if(a[i] == 'a' or a[i] == 'e' or a[i] == 'i' or a[i] == 'o' or a[i] == 'u'):
		count +=1
print(count)
