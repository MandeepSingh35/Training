key = input("Welcome User..! Press 'y' to Continue, Other Key to Exit. ")
match = lambda pin: pins == pin
pins=[1474,1235,6978,6936]
count = 0
if( key != "y"):
	exit()
else:
	pin = int(input("Enter ATM Pin : "))
	print(pins)
	#for count in range(0,3):
	
	for i in range(0,4):
		if(count < 3 ):
			if(pin == pins[i]):
				print(pins[i])
				print("Match Found")
				count +=1
				break
			elif(pin != pins[i]):
				print(pins[i])
				pin = input("Please try again")
				count +=1
				break
			else:
				print("Tera sir")
		elif(count >= 3):
			print("Your system is blocked.Please Contact the bank!!!!!!")