import random
name= input("Player 1 Enter your name\n")
print(name + ':' + "Welcome to Snake Water Gun")
rand = ["Snake","Water","Gun"]
rand1 = random.choice(rand)

player = 0
computer=0
i = 0
ask =input("Enter Yes OR NO to play \n")
if ask == "No":
 exit()
else:
	print("Lets Begin")
while i<10:
	print(i+1, "th game")
	while 1:
		print("whats your choice\n")
		player1=input()
		if player1 == "Snake" and rand1 == "Gun":
			print("rand1 Got A point")
			computer+=1
		elif player1 == "Water" and rand1 == "Gun":
			print(name + ":" + "Got A point")
			player+=1
		elif player1 == "Gun" and rand1 =="Snake":
			print(name + ":"+ "Got A point")
			player+=1
		elif player1 == "Snake" and rand1 =="Water":
			print(name + ":"+ "Got A point")
			player+=1
		elif player1 ==  "Gun" and rand1 == "Water":
			print("Rand1 Got A point")
			computer+=1
		elif player1 == "Water" and rand1 == "Snake":
			print("Rand1 Got A point")
			computer+=1
		elif player1==rand1:
			print("OPPS NO POINT")
			break
	i+=1
print(name + "point\n",player)
print("Computer point\n",computer)
if player>computer:
	print(name + ":" + "Won the Game")
else:
	print("Computer has won the game")
exit(0)


