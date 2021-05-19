def pals():
    r = int(input("enter the range\n"))
    for i in range(r):
        num = (input("Enter the number\n"))
        org = num
        if num ==num[::-1]:
            print("The Number is Already A Palindrome")
        else:
            while 1:
                num = int(num)
                num+=1
                num=str(num)
                # nums=str(nums)
                if (num)==(num[::-1]):
                    print(f'Then Next Palidrome  of the Number you have Entered is {num}')
                    break
if __name__ =="__main__":
    print("_-----Welcome To the Palindrome Game-----_")
    pals()