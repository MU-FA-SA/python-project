temp = input("INPUT THE TEMPERATURE\n")
degree = int(temp[:-1])
i_conven = temp[-1]
if i_conven.upper() == "C":
	result = int(round((9*degree)/5+32))
elif i_conven.upper() =="F":
	result = int(round((degree-32)/5*9))
else:
	print("the input is inappropriate")
quit()
print("the out is"+ result)
