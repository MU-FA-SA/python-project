dict = { }
n = int(input("enter the number of element you want to enter\n"))
# keys =input("ENnter the key here\n")
# values = input("Enter the values here\n")

for item in range(0,n):
    keys = input("ENnter the key here\n")
    values = input("Enter the values here\n")
    dict.update({keys:values})
    print(dict)
search = input("Enter the word you want to search\n")
print(dict[search])