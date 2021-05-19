def lipali():
    mylist = []

    for i in range(int(input("Enter the Range\n"))):
        itm = int(input("Enter the Elements\n"))
        mylist.append(itm)


    for item in range(len(mylist)):
        num = mylist[item]
        num = int(num)
        if num>9:
            if str(num) == str(num)[::-1]:
                print(f"The Number is Palindrome {mylist[item]} is {mylist[item]} Itself")
            else:
                while 1:

                    num = int(num)
                    num+=1
                    num= str(num)
                    if (num)==(num[::-1]):
                        print(f'Then Next Palidrome  of the Number you have Entered is {num}')
                        break
        else:
            if num<9:
                print(f"The number is {num} smallest tha 10")

if __name__ =="__main__":
    print("----WELCOME TO THE LIST PALINDROME GAME----")
    lipali()