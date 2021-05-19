import random
def gum():
    rd = random.randint(a, b)
    guess = 0
    count = 0
    while rd!=guess and rd!= count:
        guess = int(input("Enter the guess\n"))
        if rd>guess:
            print("The Numer You Guessed  is Too Low")
            count+=1
        elif rd<guess:
            print("The Number You Guessed is Too High")
            count+=1
        else:
            if rd == guess:
                print("The Guessed Number  is Correct")
                print("-----------------------------------")
                print(f"You took {count} tries")
    return count
def gum2():
    rd1 = random.randint(a, b)
    guess1 = 0
    count1 = 0

    while rd1!=guess1 and rd1!= count1:
        guess1 = int(input("Enter the guess\n"))
        if rd1<guess1:
            print("The Number You Guessed is Too high")
            count1+=1
        elif rd1>guess1:
            print("The Number  You Guessed is Too Low")
            count1+=1
        else:
            if rd1 == guess1:
                print("The Guess You Guessed is correct")
                print("-----------------------------------")
                print(f"You took {count1} tries")
    return count1
if __name__ == "__main__":
    print("--------WELCOME TO THE GAME------------")
    ws = int(input("Press 1 to Start OR Press 2 to Exit\n"))
    if ws == 1:
        a = int(input("Enter the Minimum\n"))
        b = int(input("Enter the Maximum\n"))
        player1 = input("Player1 Enter Your Name\n").upper()
        player2 = input("Player2 Enter Your Name\n").upper()

        rad = random.randint(1,2)
        if rad == 1:
            rd = random.randint(a, b)
            print(f' {player1} will go first')

            g1 = gum()
            print('-------------------------------------------------')
            print(f" {player2} will Play Now")
            rd1 = random.randint(a, b)
            g2 = gum2()
        else:
            if rad == 2:
                rd1 = random.randint(a, b)
                print(f' {player2} will go first')

                g2 = gum2()
                rd = random.randint(a, b)
                print("-------------------------------------------")
                print(f" {player1} will Play Now")
                g1 = gum()
        if g1>g2:
            print(f"{player2} has Won The game")
        elif g2>g1:
            print(f"{player1} has Won The Game")
        else:
            print("Its a Tie")
    elif ws == 2:
        print("----------OKAY BYEE----------- ")
        exit(0)

