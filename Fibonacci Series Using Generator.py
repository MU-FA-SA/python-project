def fib(n):
    # n = int(input("Enter the NUmber\n"))
    a = 0
    b = 1
    sum = 0
    count = 1
    print(f'fibonacci series of :{n} ',end=" ")
    while count <= n:
        yield sum
        a = b
        b = sum
        sum = a + b
        if  sum == n:
            break


f = fib()
# iter = f__next__()
for i in f:
    print(i)

