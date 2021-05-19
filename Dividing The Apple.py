def div():
     n  =int(input("MUFASA Please Enter the number of Apple You have\n"))
     mn = int(input("Enter the Smallest Number\n"))
     mx = int(input("Enter the Biggest Number\n"))
     count = 0
     if mn==mx:
          print("invalid range")
     else:
          for apple in range(mn,mx):
               count+=1

               if n%apple==0:
                    print(f'The Number is Divisor by {apple}')

               elif n%apple!=0:
                    print(f"The Number is Not Divisor by {apple}")

               else:
                     print("INVALID INPUT")


if __name__=="__main__":
    div()

