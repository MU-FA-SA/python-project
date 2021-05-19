import random 
s = input("enter your name\n")
pas=len(s)
po = "".join(random.sample(s,pas))
print('the password is '+ po)