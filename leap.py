year = int(input("Enter year"))
leap = False
if(year%4 == 0 and year%100 != 0):
	if(year% 400 == 0):
		leap = False
		print("Year is leap year")
	else: 
		leap = True
		print("Year is not leap year")