import random
rd = random.randint(1,9)
guess = 0
count = 0
while count<=5 and rd!=guess:
	guess= input("Whats UR NUMBER: ")
	if guess== 'exit':
		break
	guess =  int(guess)
	if rd>guess:
		count += 1
		print("too low")
	elif rd<guess:
		count += 1
		print("too high")
	elif rd == guess:
		count += 1
		print('you got it')
		print("and you took",count,"tries")
		break
	if count >= 5:
		print("OPPS!! YOU TOOK MORE THAN",count,"TRIES")
		break