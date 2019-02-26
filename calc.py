add = lambda a,b : a+b
sub = lambda a,b : a-b
mul = lambda a,b : a*b
div = lambda a,b : a/b

num1 = int(input("Add any first number"))
ans = 0
num2 = int(input("Add any second number"))
op = input("Choose the operation to be performed by selecting +, - , *, / :")
if(op == '+'):
	ans = add(num1,num2)
	#break
elif(op == '-'):
	ans = sub(num1,num2)
	#break
elif(op == '*'):
	ans = mul(num1,num2)
	#break
elif(op == '/'):
	ans = div(num1,num2)
	#break
print(ans)
