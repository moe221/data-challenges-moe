# pylint: disable=missing-module-docstring,missing-function-docstring,eval-used
import sys
import operator

OPS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,  # use operator.div for Python 2
    '%': operator.mod,
    '^': operator.xor,
}

def main():
    """Implement the calculator"""
    return OPS[sys.argv[2]](int(sys.argv[1]), int(sys.argv[3]))


if __name__ == "__main__":
    print(main())
