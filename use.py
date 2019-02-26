pins = [(1234,1000,[+100,-200]),(1235,5000,[-100,+200]),(1236,7000,[+350,+500]),(1237,500,[-250,+450])]

m = len(pins)
for i in range(0,m):
	for j in pins:
		print(j[2]) 
		for k in j[2]:
			print(k)