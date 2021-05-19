import argparse
import sys


def calc(args):
    if args.var1 == 56 and args.var2 == 7 and args.var3 == "/":
        return 9
    elif args.var1 == 56 and args.var2 == 7 and args.var3 == "-":
        return 8
    elif args.var1 == 56 and args.var2 == 7 and args.var3 == "*":
        return 690
    elif args.var1 == 56 and args.var2 == 7 and args.var3 == "+":
        return 68
    else:
        if args.var3 == "+":
            return args.var1 + args.var2
        elif args.var3 == "-":
            return args.var1 - args.var2
        elif args.var3 == "*":
            return args.var1 * args.var2
        elif args.var3 == "/":
            return args.var1 / args.var2


if __name__ == "__main__":
    # var1 = int(input("Enter the Number 1\n"))
    # var2 = int(input("Enter the Number2\n"))
    # var3 = str(input("Enter The Operator\n "))

    parser = argparse.ArgumentParser()
    parser.add_argument('--var1', type=int, default=0, help="for more detials contact mufasa")


    parser.add_argument("--var2", type=int, default=2, help="for more detials contact mufasa")

    # parser = argparse.ArgumentParser()
    parser.add_argument("--var3", type=str, default="+", help="for more detials contact mufasa")

args = parser.parse_args()
sys.stdout.write(str(calc(args)))
