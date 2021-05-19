import re
import os
path =input("Enter your path\n")
os.chdir(path)
file1 = input("Enter the file you want to read\n")
with open(file1,"r") as f:
    fo = f.read()
    # print(fo)
patt = re.compile(r'\w+@\w+.com')
match =patt.findall(fo)
# print(match)
file2 = input("Enter the file name you want to write in\n")
with open(file2,'a') as d:
    i = 1
    for j in match:
        w =(f'Email {i} : {j}\n')
        d.write(w)
        i = i+1
print(f"Emails are : {match}")
print(f"total number of email are : {i-1}")
