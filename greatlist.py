list = ['is', 'main', 'my', 'name']
print(list)
x = len(list)
print(x)
for i in range(0,x):
	for j in range(i,x):
		if(len(list[i]) >= len(list[j])):
			#continue
			print(list[i])
	#if(b)