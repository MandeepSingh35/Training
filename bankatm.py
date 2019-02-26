def inputpin():
	pin  = int(input("Enter ATM Pin : "))
	return pin

def againpin():
	pin = input("Wrong pin. Please try again...... ")
	return pin

def wrongpin():
	print("Your account is BLOCKED. Please contact bank...... ")


def matchpin(pin):
	global count
	global b
	for i in range(0,4):
	
		for j in range(0,4):
			if(pin == pins[j]):
				b = 1
				count += 1
				break
				#return 1
			elif(pin != pins[j]) : 
				pin = againpin()
				b = 0
				count += 1
				break
			#return 0
		#elif(count >= 3):
				#wrongpin()
				#break
	return b

b = 0
count = 0
pins= [1474, 1235, 6978, 6936]
key = input("Welcome User..! Press 'y' to Continue, Other Key to Exit. ")
if(key != "y"):
	exit()
else:
	pin = inputpin()
	print(pin)
	c = matchpin(pin)
	if(c == 1):
		print("Match Found... ")
	elif(c == 0):
		print("Sorry :(")

	#if(count < 3):
		#matchpin(pin)