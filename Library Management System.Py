
new_books = []
for item in range(int(input("Enter the number of books\n"))):
    new_books.append(input("Enter the books name\n").upper())
print(new_books)
# lenddata = {}
# for i in range(int(input("Enter the number of element\n"))):
#     member = input("Enter the Your Name\n").upper()
#     lend_book = input("Enter the Name of Book You Want to Lend\n").upper()
#     lenddata.update({lend_book: member})
#     print(lenddata)


class Library:
    def __init__(self,library_name,aname):
        self.new_books = []
        self.lb =library_name
        self.admin =aname
    def printdetials(self):
       return f"Welcome to {self.lb},Created by {self.admin} "
    # global new_books

    @classmethod
    def display(cls,new_books):
        print(f'The Books which are Available{new_books}')
    @classmethod
    def add(cls,new_books):
        book = (input("Enter the Name of the Book you want to ADD\n")).upper()
        if book not in new_books:
            new_books.append(book)
            print(new_books)
        elif book in new_books:
            print("Already there")
            print(new_books)
        else:
            print("INValid Entry")
# lenddata = {}
# for i in range(int(input("Enter the number of element\n"))):
#     member = input("Enter the Your Name\n").upper()
#     lend_book = input("Enter the Name of Book You Want to Lend\n").upper()
#     lenddata.update({lend_book: member})


    @classmethod
    def lend(cls,my_books,**lenddata):
        # def d(**lenddata):
        lenddata = {}
        for i in range(int(input("Enter the number of element\n"))):
            member = input("Enter the Your Name\n").upper()
            lend_book =input("Enter the Name of Book You Want to Lend\n").upper()
            lenddata.update({lend_book: member})
            print(lenddata)


        # lenddata.update({lend_book:member})
        # print(lenddata)

        # for i in range(int(input("Enter the number of element\n"))):
        if lend_book in new_books:
            new_books.remove(lend_book)
            print(new_books)
        else:
            print("Invalid Entry")
        # for lend_book,member in lenddata:
        #     lenddata.update({lend_book: member})
        print (lenddata)
    @classmethod
    def ret(cls,new_books):

        member = input("Enter your name\n").upper()
        returnbook = input("Enter the book you want to return\n").upper()
        if returnbook not in new_books:
            new_books.append(returnbook)
            # lenddata.remove(returnbook)
            print (f"the book {returnbook} is return by {member}")
            print(new_books)
            # print(lenddata)
        elif returnbook in new_books:
            print("Already there")
            print(new_books)
        else:
            print("INValid Entry")
admin = Library("VIDYA'S","IBRAHIM")
secret_key ="66866"
if __name__ == "__main__":
    key = input("enter the password\n")
    if key== secret_key:
        print(f"Welcome to My {admin.printdetials()}")
        print("Type 'DS' to view books\nType 'L' to lend books\nType 'A' to add books\nType 'R' to return books\nType 'Q' to quit library")
        while True:
            dec = input("Enter your choice\n")
            if dec.upper() == "DS":
                admin.display(new_books)
            elif dec.upper() == "L":
                admin.lend(new_books)
            elif dec.upper() == "A":
                admin.add(new_books)
            elif dec.upper() == "R":
                admin.ret(new_books)
            elif dec.upper() == "QUIT":
                new_books = new_books
                break
    else:
        print("Wrong input")



