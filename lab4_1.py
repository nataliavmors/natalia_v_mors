import sys
import argparse

def fib(n):
    a = 1
    if n > 2:
        a = fib(n - 1) + fib(n - 2)
    return a

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', default=1, type=int)
    return parser


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
    val = fib(namespace)
    print(val)