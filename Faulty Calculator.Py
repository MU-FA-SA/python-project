var1 = int(input("Enter the Number 1\n"))
var2 = int(input("Enter the Number2\n"))
var3 = str(input("Enter The Operator\n "))
if var1==56 and var2 == 7 and var3 == "/":
	print("8")
elif var1 == 56 and var2 == 7 and var3 == "-":
	print("48")
elif var1 == 56 and var2 == 7 and var3 == "*":
	print("690")
elif var1 == 56 and var2 == 7 and var3 == "+":
	print("68")
else:
	if var3=="+":
	    print(var1+var2)
	elif var3 =="-":
		print(var1-var2)
	elif var3 =="*":
		print(var1*var2)
	elif var3 =="/":
		print(var1/var2)
	else:
		print("NOT A NUMBER")