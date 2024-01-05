#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv
<<<<<<< HEAD

=======
>>>>>>> origin/master
if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage:", argv[0], "<a> <operator> <b>")
        exit(1)
<<<<<<< HEAD

=======
>>>>>>> origin/master
    op = argv[2]
    f = {"+": add, "-": sub, "*": mul, "/": div}
    if op not in f:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
<<<<<<< HEAD

=======
>>>>>>> origin/master
    a = int(argv[1])
    b = int(argv[3])
    print("{:d} {:s} {:d} = {:d}".format(a, op, b, f[op](a, b)))
