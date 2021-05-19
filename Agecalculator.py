
def dateof():
    wet = int(input("enter the year of birth\n"))
    eet  =(input("Press 1 if you want to check in a particular year or 2 to know the year of 100\n"))
    if eet=='1':
        eet =  int(input("Enter the year you want to check\n"))
        print(eet-wet)
    elif eet == "2":
        print(f'you will 100 in {wet+100}')
    elif wet<120:
        print (120-wet)
    elif wet<1910:
        print("You are the Oldest Person On the Earth Show me the pic of yours with Gandhi.ji ")
    else:
        print("invalid entry")

def age():
    wet = int(input("Enter Your Age\n"))
    eet = (input("Press 1 if you want to check in a particular year or 2 to know year of 100\n"))
    wwet = 2019-wet
    if eet=='1':
        eet =  int(input("Enter the year you want to check\n"))
        print(eet-wwet)
    elif eet == "2":
        print(f'you will 100 in {wwet+100}')
    elif wet<120:
        print (120-wwet)
    elif wet>110:
        print("You are the Oldest Person On the Earth Show me the pic of yours with Gandhi.ji ")
    else:
        print("invalid entry")
if __name__ =="__main__":
    it =  int(input("Press 1 to Enter Age OR Press 2 to Enter Date Of Birth \n"))
    if it == 1:
        dateof()
        exit(0)
    else:
        age()
        exit(0)