import random
def rohan():
    global rh_list
    rh_list = []
    global n
    n =int(input("ENter the range\n"))
    for i in range(1,n):
        rad = random.randint(1, 5)
        if i == 1 or i == 3 or i == 5 or i == 7:
            e = a*i
            rh_list.append(e)
        elif i ==2 or i ==4 or i==10:

            e = a*i
            rh_list.append(e)
        elif i == 6 or i == 8 or i == 9:
            e = a*i+rad
            rh_list.append(e)
    print(rh_list)
    return rh_list

def my_check():
    global chec_list
    chec_list = []
    for i in range(1,n):
        d = a*i
        chec_list.append(d)
    print(chec_list)
    return chec_list














if __name__ == "__main__":
    a = int(input("Enter the Number\n"))
    rohan()
    my_check()
    while True:
        idx = 0
        result = []
        for i in rh_list:

            if i == chec_list[idx]:
                print(f"THE Values is correct {idx, i}")
                idx += 1
            elif i != chec_list[idx]:
                print(f'The Value which is not Correct is At  {idx} And The {i} is the Value')
                idx += 1
            else:
                pass
        break