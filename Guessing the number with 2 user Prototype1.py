import random
rad  =  random.randint(1,2)


def gum(a, b, rd):
    guess = 0
    count = 0

    while rd != guess and rd != count:

        guess = int(input("Enter the guess\n"))

        if rd > guess:
            print("THE NUMBER IS TOO LOW")
            count += 1
        elif rd < guess:
            print("The NUMBER IS TOO HIGH")
            count += 1
        else:
            if rd == guess:
                print(f'YOU TOOK {count} TRIES')

    return count


if __name__ == "__main__":
    ws = int(input('Press 1 to start the Game OR press 2 to exit\n'))


    if ws == 1:
        print("-----Welcome to the Guessing The Number Game---")
        a = int(input("ENTER THE MINIMUM NUMBER\n"))
        b = int(input("ENTER THE MAXIMUM NUMBER\n"))
        print("The Game is started")
        player1 = input("Enter your Name\n").upper()
        print(f"{player1} will go First")
        print(f"Please guess the Number between {a} and {b}")
        rd1 = random.randint(a, b)
        g1 = gum(a, b, rd1)
        # if turn =='player2':
        print("Player 2 Will Play")
        player2 = input("Enter your Name\n").upper()
        print(f'{player2} will go Second')
        print(f"Please guess the Number between {a} and {b}")
        rd = random.randint(a, b)
        g2 = gum(a, b, rd)
        if g1 < g2:
                print("Player 1 has Won the Game")

        if g1 > g2:
            print("Player 2 has Won the Game")
        else:
            print("Its a tie")

    elif ws ==2:
        exit(0)

#     else:
#         exit(0)
#     # break
