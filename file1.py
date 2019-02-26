words = ["Fool","Idiot","Stupid","Dumb","Bitch"]
obj1=open("abcd.txt","r")
s=obj1.read()  
#s = str(s)
#print ("kkkk",s)
obj1.close()
obj1=open("abcd.txt","w")
b = s.split()
for k in b:
	#print (k)
	#for i in words:
	#	print(i)
	if(k in words):
		#print("if chlya")
		m = len(k)
		#print(m)
		for j in range(0,m):
			#print("for j aala chlya")
			obj1.write("*"*m)
			obj1.write(" ")
			#print("*"*m)
			break
	elif(b != k):
			#print("elif chlya")
			#print(k)
			obj1.write(k)
			obj1.write(" ")
			#print(b)
	elif(b == " "):
		obj1.write(" ")

print("Done!!! Please check the file again...")

obj1.close()