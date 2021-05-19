import datetime
def gettime():
	return datetime.datetime.now()
def update():
	i = int(input("Press 1 for Food Press 2 for Exercise\n"))
	k = int(input("Press 1 for Nadim\n""Press 2 for Sohail\n" "Press 3 for Junaid Suwar\n"))
	if i ==1 and k ==1:
		value=input("Enter Value\n")
		with open("nadim.txt",'a') as op:
			op.write(str([str(gettime())]) + ": " + value + "\n")
		print("successfully written")
	elif i==1 and k==2:
		value=input("Enter Value\n")
		with open("sohail.txt",'a') as op:
			op.write(str([str(gettime())]) + ": " + value + "\n")
		print("successfully written")
	elif i==1 and k==3:
		value=input("Enter Value\n")
		with open("junaid.txt",'a') as op:
			op.write(str([str(gettime())]) + ": " + value + "\n")
		print("successfully written")
	elif i==2 and k==1:
		value=input("Enter Value\n")
		with open("nadim-ex.txt",'a') as op:
			op.write(str([str(gettime())]) + ": " + value + "\n")
		print("successfully written")
	elif i==2 and k==2:
		value=input("Enter Value\n")
		with open("sohail-ex.txt",'a') as op:
			op.write(str([str(gettime())]) + ": " + value + "\n")
		print("successfully written")
	elif i==2 and k==3:
		value=input("Enter Value\n")
		with open("junaid-ex.txt",'a') as op:
			op.write(str([str(gettime())]) + ": " + value + "\n")
		print("successfully written")
	else:
		print ("Invalid Input")
def retirve():
	i = int(input("Enter The number 1 for Food and 2 for Exercise\n"))
	k = int(input("Enter 1 for Nadim 2\n" "Press 2 for Sohail\n" "Press 3 for junaid Suwar\n"))
	if i==1 and k==1:
		with open("nadim.txt",'r') as op:
			for i in op:
				print(i,end=" ")
	elif i==1 and k==2:
		with open("sohail.txt",'r') as op:
			for i in op:
				print(i,end="")
	elif  i==1 and k==3:
		with open("junaid.txt",'r') as op:
			for i in op:
				print(i,end="")
	elif i==2 and k==1:
		with open("nadim-ex.txt",'r') as op:
			for i in op:
				print(i,end="")
	elif i ==2 and k==2:
		with open("sohail-ex.txt",'r') as op:
			for i in op:
				print(i,end="")
	elif i==2 and k==3:
		with open("junaid-ex.txt",'r') as op:
			for i in op:
				print(i,end="")
	else:
		print("INvalid INput")
print("health management system: ")
a=int(input("press 1 for Update the value and 2 for Retirve\n"))

if a==1:
	update()
else:
	retirve()                       



