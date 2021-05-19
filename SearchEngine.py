my_list = []
for i in range(int(input("Enter the Number Of Element You Want to Enter\n"))):
    b = input("Enter The Word You Want to Add\n")
    my_list.append(b)
    print(my_list)
def sear():
    c = list()
    relevance = 0
    d =list()
    j =1
    result = 0
    s = input('Enter the Word You want to search\n')
    for i in my_list:
        c = i.split()
        for t in c:
            if t.lower() == s.lower():
                if relevance >= 2:
                    d.insert(0, i)
                    break
                else:
                    # time.sleep(0.1)
                    d.insert(j, i)
                    j += 1

                result += 1
                relevance += 1

            else:
                pass
    d.pop(len(d) - 1)
    print(f'{result} results found: ')
    print(d)












if __name__ == "__main__":
    print("Welcome To The Search Engine")
    print('-----------------------------')
    a = int(input("Press 1 to Search\nPress 3 to Exit\n"))
    if a == 1:
        sear()
    elif a==2:
        exit(0)
